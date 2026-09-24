// Unit tests for the pure functions in apps-script/venus-script.js:
// stage classification, the forward-only rank guard, identity building,
// hashing, normalisation and the payload privacy contract.
//
//   node test/units.cjs
const crypto = require('crypto'), fs = require('fs'), path = require('path');

const SCRIPT = path.join(__dirname, '..', 'apps-script', 'venus-script.js');
const TMP    = path.join(__dirname, '.units_t.cjs');

global.Utilities = {
  DigestAlgorithm: { SHA_256: 'sha256' },
  Charset: { UTF_8: 'utf8' },
  // Apps Script returns SIGNED bytes. The script has to mask with & 0xFF.
  computeDigest: (a, s) =>
    Array.from(crypto.createHash('sha256').update(s, 'utf8').digest())
         .map(b => b > 127 ? b - 256 : b)
};

const src = fs.readFileSync(SCRIPT, 'utf8');
fs.writeFileSync(TMP,
  src + '\nmodule.exports={classify,buildUserData,normPhone,normEmail,splitName,normName,sha256,stageTime,STAGE_RANK,CRM_NAME,API_VERSION};');
const M = require(TMP);

let pass = 0, fail = 0;
const t = (l, g, w) => {
  if (JSON.stringify(g) === JSON.stringify(w)) pass++;
  else { fail++; console.log('FAIL ' + l + '\n     got  ' + JSON.stringify(g) + '\n     want ' + JSON.stringify(w)); }
};

// ---- stage classification against every real status seen in the live sheet ----
t('complete',       M.classify('Booked','Complete'),      'ShowedUp');
t('arrived',        M.classify('Booked','Arrived'),       'ShowedUp');
t('running late',   M.classify('Booked','Running Late'),  'ShowedUp');
t('messy case',     M.classify('booked','  COMPLETE  '),  'ShowedUp');
t('no show',        M.classify('Booked','No Show'),       'NoShow');
t('not show',       M.classify('Booked','Not Show'),      'NoShow');
t('waiting',        M.classify('Booked','Waiting'),       'ScheduledAppointment');
t('manual review',  M.classify('Booked','Manual Review'), 'ScheduledAppointment');
t('booked only',    M.classify('Booked',''),              'ScheduledAppointment');
t('not interested', M.classify('Not Interested',''),      'Disqualified');
t('no contact -> raw', M.classify('No Contact',''),       null);
t('call later -> raw', M.classify('Call Later',''),       null);
t('nulls -> raw',      M.classify(null,null),             null);

// ---- the funnel must only move FORWARD ----
const R = M.STAGE_RANK;
t('Lead is first',            R.Lead, 1);
t('Scheduled above Lead',     R.ScheduledAppointment > R.Lead, true);
t('ShowedUp is top',          R.ShowedUp > R.ScheduledAppointment, true);
t('NoShow above Scheduled',   R.NoShow > R.ScheduledAppointment, true);
t('ShowedUp beats NoShow',    R.ShowedUp > R.NoShow, true);
t('Disqualified above Lead',  R.Disqualified > R.Lead, true);

// simulate the guard the main loop uses
const advances = (last, next) => !(last === next) &&
  !(last && R[last] && R[next] && R[next] <= R[last]);
t('Lead -> Scheduled sends',        advances('Lead','ScheduledAppointment'), true);
t('Scheduled -> ShowedUp sends',    advances('ScheduledAppointment','ShowedUp'), true);
t('Scheduled -> NoShow sends',      advances('ScheduledAppointment','NoShow'), true);
t('ShowedUp -> ShowedUp blocked',   advances('ShowedUp','ShowedUp'), false);
t('ShowedUp -> Scheduled blocked',  advances('ShowedUp','ScheduledAppointment'), false);
t('ShowedUp -> NoShow blocked',     advances('ShowedUp','NoShow'), false);
t('NoShow -> ShowedUp sends',       advances('NoShow','ShowedUp'), true);
t('blank -> Lead sends',            advances('','Lead'), true);
t('Lead -> Lead blocked',           advances('Lead','Lead'), false);

// ---- identity ----
const LEAD = '9001000000000099';
const ud = M.buildUserData(LEAD,'someone@example.com','+923001234567','Some One');
t('lead_id is string',  typeof ud.lead_id, 'string');
t('lead_id exact',      ud.lead_id, LEAD);
t('lead_id no precision loss', String(ud.lead_id), LEAD);
t('20-digit id survives', M.buildUserData('12345678901234567890','','','X').lead_id, '12345678901234567890');
t('em array',  Array.isArray(ud.em), true);
t('ph array',  Array.isArray(ud.ph), true);
t('em value',  ud.em[0], crypto.createHash('sha256').update('someone@example.com').digest('hex'));
t('ph value',  ud.ph[0], crypto.createHash('sha256').update('923001234567').digest('hex'));
t('form vs pabau phone collide',
  M.buildUserData('','','+92300-1234567','X').ph[0],
  M.buildUserData('','','+923001234567','X').ph[0]);
t('nothing -> null', M.buildUserData('','','',''), null);
t('junk id -> null', M.buildUserData('abc','','','X'), null);
t('lead id only',    typeof M.buildUserData(LEAD,'','','').lead_id, 'string');

// ---- stage timing ----
const need = { updated: 0 }, nice = { leadDate: 1 };
const rowA = [new Date('2026-08-12T10:00:00Z'), new Date('2026-08-10T09:00:00Z')];
t('ShowedUp uses pabau ts', M.stageTime('ShowedUp', rowA, need, nice).toISOString(),
  new Date('2026-08-12T10:00:00Z').toISOString());
t('Lead uses lead date',    M.stageTime('Lead', rowA, need, nice).toISOString(),
  new Date('2026-08-10T09:00:00Z').toISOString());
const rowB = ['', ''];
t('missing ts falls back to now', Math.abs(M.stageTime('ShowedUp', rowB, need, nice) - Date.now()) < 5000, true);
t('no leadDate column ok', Math.abs(M.stageTime('Lead', rowB, need, {leadDate:-1}) - Date.now()) < 5000, true);

// ---- normalisation ----
t('local 0310',  M.normPhone('0310-0875614'), '923100875614');
t('spaces',      M.normPhone('+92 310 087 5614'), '923100875614');
t('email lower', M.normEmail('  TestUser@Example.COM '), 'testuser@example.com');
t('name strip',  M.normName('MiXeD_cAsE'), 'mixedcase');
t('3-part last', M.splitName('First Middle Last').ln, 'Last');

// ---- config ----
t('API v26.0', M.API_VERSION, 'v26.0');
t('CRM name',  typeof M.CRM_NAME, 'string');

// ---- privacy: only lead_id may be unhashed ----
t('no raw PII', Object.entries(ud).filter(([k,v]) =>
  k !== 'lead_id' && !(Array.isArray(v) && v.every(x => /^[a-f0-9]{64}$/.test(x)))), []);

try { fs.unlinkSync(TMP); } catch (e) {}
console.log('\nunits: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
