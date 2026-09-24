// End-to-end harness for apps-script/venus-script.js
// Fakes SpreadsheetApp, UrlFetchApp, PropertiesService and Logger, then runs the
// REAL sendStagesToMeta across simulated multi-tab sheets and checks both what
// Meta would receive and what the sheet looks like afterwards.
//
//   node test/harness.cjs
const crypto = require('crypto'), fs = require('fs'), path = require('path');

const SCRIPT = path.join(__dirname, '..', 'apps-script', 'venus-script.js');
const TMP    = path.join(__dirname, '.venus_t.cjs');

let LOG = [];
global.Logger = { log: m => LOG.push(String(m)) };
global.Utilities = {
  DigestAlgorithm: { SHA_256: 'sha256' }, Charset: { UTF_8: 'utf8' },
  // Apps Script returns SIGNED bytes. Reproduce that exactly.
  computeDigest: (a, s) => Array.from(crypto.createHash('sha256').update(s, 'utf8').digest())
                                .map(b => b > 127 ? b - 256 : b)
};
global.PropertiesService = { getScriptProperties: () => ({ getProperty: k => k === 'META_TOKEN' ? 'FAKE' : null }) };

let POSTS = [], NEXT_CODE = 200, SETVALUES_CALLS = 0;
global.UrlFetchApp = { fetch: (url, opt) => {
  const body = JSON.parse(opt.payload);
  POSTS.push({ url, n: body.data.length, data: body.data, hasToken: !!body.access_token,
               testCode: body.test_event_code });
  const code = NEXT_CODE;
  return { getResponseCode: () => code,
           getContentText: () => JSON.stringify({ events_received: body.data.length, messages: [] }) };
}};

function makeSheet(name, grid) {
  return {
    _g: grid, getName: () => name,
    getLastRow: () => grid.length, getLastColumn: () => grid[0] ? grid[0].length : 0,
    getDataRange: () => ({ getValues: () => grid.map(r => r.slice()) }),
    getRange: (row, col, nr, nc) => ({
      getValues: () => { const o = []; for (let r = 0; r < (nr || 1); r++) {
          const src = grid[row - 1 + r] || []; o.push(src.slice(col - 1, col - 1 + (nc || 1))); } return o; },
      setValues: v => { SETVALUES_CALLS++;
        for (let r = 0; r < v.length; r++) { if (!grid[row - 1 + r]) grid[row - 1 + r] = [];
          for (let c = 0; c < v[r].length; c++) grid[row - 1 + r][col - 1 + c] = v[r][c]; } },
      setValue: v => { SETVALUES_CALLS++; if (!grid[row - 1]) grid[row - 1] = []; grid[row - 1][col - 1] = v; }
    })
  };
}

const D = n => { const d = new Date(); d.setDate(d.getDate() - n); return d; };
const iso = d => { const p = x => String(x).padStart(2, '0');
  return d.getFullYear()+'-'+p(d.getMonth()+1)+'-'+p(d.getDate())+' '+p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds()); };

const HEAD = [' Date','Full Name','Booked Status','Pabau Status','CONSULATION STATUS UPDATED AT',
              'Meta Lead ID','Lead Phone','Lead Email','Pabau Client Mobile','Pabau Client Email','Meta Stage Sent'];

const demoRows = () => [
 [iso(D(1)),'Ayesha Khan','No Contact','','','9001000000000001','+92300-1111111','ayesha.khan@example.com','','',''],
 [iso(D(1)),'Bilal Ahmed','Call Later','','','9001000000000002','+92301-2222222','bilal.ahmed@example.com','','',''],
 [iso(D(2)),'Sana Malik','Booked','','','9001000000000003','+92302-3333333','sana.malik@example.com','','',''],
 [iso(D(3)),'Usman Tariq','Booked','Waiting','','9001000000000004','+92303-4444444','usman.tariq@example.com','','',''],
 [iso(D(3)),'Hina Raza','Booked','Complete',iso(D(1)),'9001000000000005','+92304-5555555','hina.raza@example.com','+92304-5555555','hina.raza@example.com',''],
 [iso(D(4)),'Omar Sheikh','Booked','Arrived',iso(D(2)),'9001000000000006','+92305-6666666','omar.sheikh@example.com','+92305-6666666','omar.sheikh@example.com',''],
 [iso(D(4)),'Zara Iqbal','Booked','No Show',iso(D(2)),'9001000000000007','+92306-7777777','zara.iqbal@example.com','+92306-7777777','zara.iqbal@example.com',''],
 [iso(D(5)),'Kamran Butt','Not Interested','','','9001000000000008','+92307-8888888','kamran.butt@example.com','','',''],
 [iso(D(2)),'Nadia Aslam','Booked','','','','','','','',''],
 [iso(D(3)),'Faisal Qureshi','Booked','Complete',iso(D(1)),'9001000000000010','+92309-9999999','faisal.q@example.com','','','ShowedUp'],
 [iso(D(3)),'Rabia Noor','Booked','Complete',iso(D(1)),'9001000000000011','+92310-1010101','rabia.noor@example.com','','','ScheduledAppointment'],
 [iso(D(20)),'Old Record','Booked','Complete',iso(D(20)),'9001000000000012','+92311-1111000','old.record@example.com','','',''],
];

let tabA, tabB, tabC, tabD;
function freshBook(){
  tabA = makeSheet('Islamabad Logic', [HEAD.slice(), ...demoRows()]);
  tabB = makeSheet('Lahore Logic', [HEAD.slice(),
    [iso(D(1)),'Sara Ali','Booked','Complete',iso(D(1)),'9002000000000001','+92321-1234567','sara.ali@example.com','','',''],
    [iso(D(1)),'Ali Hassan','No Contact','','','9002000000000002','+92322-1234567','ali.hassan@example.com','','',''],
    [iso(D(2)),'Mehwish Q','Booked','No Show',iso(D(1)),'9002000000000003','+92323-1234567','mehwish@example.com','','',''],
  ]);
  tabC = makeSheet('Summary', [['Branch','Total'],['Islamabad',100]]);   // not a lead tab
  tabD = makeSheet('Karachi Logic', [HEAD.slice(0,10),                   // missing stage column
    [iso(D(1)),'X Y','Booked','','','9003000000000001','+92300-0000000','x@example.com','','']]);
  global.SpreadsheetApp = { getActive: () => ({
    getSheetByName: n => ({'Islamabad Logic':tabA,'Lahore Logic':tabB,'Summary':tabC,'Karachi Logic':tabD}[n] || null),
    getSheets: () => [tabA, tabB, tabC, tabD] }) };
}

function load(overrides){
  let src = fs.readFileSync(SCRIPT, 'utf8');
  for (const [k, v] of Object.entries(overrides || {}))
    src = src.replace(new RegExp('const ' + k + '\\s*=\\s*[^;]+;'), 'const ' + k + ' = ' + v + ';');
  fs.writeFileSync(TMP, src + '\nmodule.exports={sendStagesToMeta,listTabs,addStageColumnEverywhere,' +
    'classify,buildUserData,normPhone,normEmail,splitName,normName,sha256,stageTime,STAGE_RANK,CRM_NAME,API_VERSION};');
  delete require.cache[require.resolve(TMP)];
  return require(TMP);
}

let pass = 0, fail = 0;
const t = (l, g, w) => { if (JSON.stringify(g) === JSON.stringify(w)) { pass++; }
  else { fail++; console.log('FAIL ' + l + '\n     got  ' + JSON.stringify(g) + '\n     want ' + JSON.stringify(w)); } };
const reset = () => { LOG = []; POSTS = []; SETVALUES_CALLS = 0; NEXT_CODE = 200; freshBook(); };
const line = re => LOG.find(l => re.test(l)) || '';

// ---------- 1. DRY RUN, single tab ----------
reset();
let M = load({ DRY_RUN: 'true', SHEET_NAMES: "['Islamabad Logic']" });
M.sendStagesToMeta();
t('dry: no HTTP call', POSTS.length, 0);
t('dry: no sheet write', SETVALUES_CALLS, 0);
t('dry: counts line', /to send: 9 .*"Lead":2.*"ScheduledAppointment":2.*"ShowedUp":3.*"NoShow":1.*"Disqualified":1/.test(line(/to send:/)), true);
t('dry: with lead_id 9', /with lead_id: 9/.test(line(/to send:/)), true);
t('dry: unchanged 1',   /stage unchanged: 1/.test(line(/to send:/)), true);
t('dry: no identity 1', /no identity: 1/.test(line(/to send:/)), true);
t('dry: too old 1',     /older than 7 days: 1/.test(line(/to send:/)), true);
t('dry: optional cols logged', /optional columns found: leadId, leadPhone, leadEmail, leadDate, pabauPhone, pabauEmail/.test(line(/optional columns/)), true);

// ---------- 2. LIVE, single tab ----------
reset();
M = load({ DRY_RUN: 'false', SHEET_NAMES: "['Islamabad Logic']" });
M.sendStagesToMeta();
t('live: one batch', POSTS.length, 1);
t('live: 9 events', POSTS[0].n, 9);
t('live: token attached', POSTS[0].hasToken, true);
t('live: no test code sent', POSTS[0].testCode, undefined);
t('live: url', POSTS[0].url, 'https://graph.facebook.com/v26.0/726819547675464/events');
t('live: ONE setValues per tab', SETVALUES_CALLS, 1);
t('live: column K after run', tabA._g.slice(1).map(r => r[10]),
  ['Lead','Lead','ScheduledAppointment','ScheduledAppointment','ShowedUp','ShowedUp','NoShow','Disqualified','','ShowedUp','ShowedUp','']);
t('live: done line', /DONE\. sent and marked: 9/.test(line(/DONE/)), true);

// payload contract
const ev = POSTS[0].data[0];
t('payload: action_source', ev.action_source, 'system_generated');
t('payload: event_source', ev.custom_data.event_source, 'crm');
t('payload: lead_event_source', ev.custom_data.lead_event_source, 'Venus Lead Flow');
t('payload: em is array', Array.isArray(ev.user_data.em), true);
t('payload: lead_id is string', typeof ev.user_data.lead_id, 'string');
t('payload: country hashed', ev.user_data.country[0], crypto.createHash('sha256').update('pk').digest('hex'));
t('payload: no raw PII', Object.entries(ev.user_data).filter(([k,v]) =>
  k !== 'lead_id' && !(Array.isArray(v) && v.every(x => /^[a-f0-9]{64}$/.test(x)))), []);

// ---------- 3. second run sends nothing ----------
POSTS = []; LOG = []; SETVALUES_CALLS = 0;
M.sendStagesToMeta();
t('rerun: no HTTP call', POSTS.length, 0);
t('rerun: to send 0', /to send: 0 /.test(line(/to send:/)), true);
t('rerun: unchanged 10', /stage unchanged: 10/.test(line(/to send:/)), true);

// ---------- 4. MULTI TAB ----------
reset();
M = load({ DRY_RUN: 'false', SHEET_NAMES: "['Islamabad Logic','Lahore Logic']" });
M.sendStagesToMeta();
t('multi: single batch', POSTS.length, 1);
t('multi: 12 events', POSTS[0].n, 12);
t('multi: two setValues, one per tab', SETVALUES_CALLS, 2);
t('multi: tab B column K', tabB._g.slice(1).map(r => r[10]), ['ShowedUp','Lead','NoShow']);
t('multi: tab A untouched by B', tabA._g[2][10], 'Lead');

// ---------- 5. bad tab names and missing columns ----------
reset();
M = load({ DRY_RUN: 'true', SHEET_NAMES: "['Islamabad Logic','Karachi Logic','Nope Tab']" });
M.sendStagesToMeta();
t('bad: warns missing column', /Karachi Logic skipped, missing column: Meta Stage Sent/.test(line(/Karachi/)), true);
t('bad: warns absent tab', /no tab named Nope Tab/.test(line(/Nope Tab/)), true);
t('bad: still processes good tab', /to send: 9 /.test(line(/to send:/)), true);

// ---------- 6. failed batch must NOT mark rows ----------
reset();
M = load({ DRY_RUN: 'false', SHEET_NAMES: "['Islamabad Logic']" });
NEXT_CODE = 400;
M.sendStagesToMeta();
t('fail: no sheet write', SETVALUES_CALLS, 0);
t('fail: column K untouched', tabA._g[1][10], '');
t('fail: logs retry', /batch failed, rows NOT marked/.test(line(/batch failed/)), true);
t('fail: sent 0', /DONE\. sent and marked: 0/.test(line(/DONE/)), true);

// ---------- 7. batching over 100 ----------
reset();
const big = [HEAD.slice()];
for (let i = 0; i < 250; i++)
  big.push([iso(D(1)), 'P' + i, 'Booked', 'Complete', iso(D(1)), '95000000000' + String(i).padStart(4,'0'),
            '+9230' + String(i).padStart(8,'0'), 'p' + i + '@example.com', '', '', '']);
tabA = makeSheet('Islamabad Logic', big);
global.SpreadsheetApp = { getActive: () => ({ getSheetByName: n => n === 'Islamabad Logic' ? tabA : null,
                                              getSheets: () => [tabA] }) };
M = load({ DRY_RUN: 'false', SHEET_NAMES: "['Islamabad Logic']" });
M.sendStagesToMeta();
t('batch: three calls', POSTS.length, 3);
t('batch: sizes', POSTS.map(p => p.n), [100, 100, 50]);
t('batch: all rows marked', tabA._g.slice(1).every(r => r[10] === 'ShowedUp'), true);
t('batch: 3 column writes not 250', SETVALUES_CALLS, 3);

// ---------- 8. MAX_EVENTS_PER_RUN brake ----------
reset();
tabA = makeSheet('Islamabad Logic', big.map(r => r.slice()));
tabA._g.slice(1).forEach(r => r[10] = '');
global.SpreadsheetApp = { getActive: () => ({ getSheetByName: n => n === 'Islamabad Logic' ? tabA : null,
                                              getSheets: () => [tabA] }) };
M = load({ DRY_RUN: 'false', SHEET_NAMES: "['Islamabad Logic']", MAX_EVENTS_PER_RUN: '120' });
M.sendStagesToMeta();
t('cap: only 120 sent', POSTS.reduce((a, p) => a + p.n, 0), 120);
t('cap: logged', /CAPPED at 120/.test(line(/to send:/)), true);
t('cap: leftovers unmarked', tabA._g.slice(1).filter(r => r[10] === '').length, 130);

// ---------- 9. listTabs and addStageColumnEverywhere ----------
reset();
M = load({ DRY_RUN: 'true', SHEET_NAMES: "['Islamabad Logic']" });
LOG = []; M.listTabs();
t('listTabs: marks ready',   /"Islamabad Logic"  rows: 12  READY/.test(line(/Islamabad/)), true);
t('listTabs: marks missing', /"Karachi Logic".*MISSING -> Meta Stage Sent/.test(line(/Karachi/)), true);
t('listTabs: non lead tab',  /"Summary".*MISSING/.test(line(/Summary/)), true);
LOG = []; M.addStageColumnEverywhere();
t('addCol: added to Karachi', tabD._g[0][10], 'Meta Stage Sent');
t('addCol: left Summary alone', tabC._g[0].length, 2);
t('addCol: skipped ones that had it', /"Islamabad Logic" already has it/.test(line(/Islamabad/)), true);
t('addCol: count', /tabs updated: 1/.test(line(/tabs updated/)), true);

try { fs.unlinkSync(TMP); } catch (e) {}
console.log('\nharness: ' + pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
