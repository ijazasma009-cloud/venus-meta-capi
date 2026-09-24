/**** SANDBOX BUILD. Points at the test dataset, not Venus.
      Single tab. Use this to rehearse the whole thing on a throwaway account. ****/

/**** CONFIG ****/
const DATASET_ID      = '1612027523775772';   // TEST dataset only
const SHEET_NAME      = 'Demo';               // the tab name in the demo sheet
const API_VERSION     = 'v26.0';
const DRY_RUN         = true;    // Part 6 tells you when to change this
const TEST_EVENT_CODE = '';      // CRM events have no test code, leave empty
const MAX_AGE_DAYS    = 7;       // Meta rejects events older than this
const COUNTRY         = 'pk';
const CRM_NAME        = 'Sheet CRM Test';     // shown in Meta as the source name

// Required columns. Script stops if any are missing.
const NEED = {
  booked : 'Booked Status',
  pabau  : 'Pabau Status',
  updated: 'CONSULATION STATUS UPDATED AT',
  name   : 'Full Name',
  stage  : 'Meta Stage Sent'      // stores the LAST stage sent for this lead
};

// Optional. Used when present.
const NICE = {
  leadId    : 'Meta Lead ID',
  leadPhone : 'Lead Phone',
  leadEmail : 'Lead Email',
  leadDate  : ' Date',               // note the leading space
  pabauPhone: 'Pabau Client Mobile',
  pabauEmail: 'Pabau Client Email'
};

// Meta needs the WHOLE funnel, including the raw lead stage.
// Rank stops a lead moving backwards if a status is edited by hand.
const STAGE_RANK = {
  Lead: 1,
  ScheduledAppointment: 2,
  Disqualified: 3,
  NoShow: 3,
  ShowedUp: 4
};

/**** MAIN ****/
function sendStagesToMeta() {
  const token = PropertiesService.getScriptProperties().getProperty('META_TOKEN');
  if (!token) { Logger.log('STOP: META_TOKEN not set. See Part 4.2.'); return; }

  const sh = SpreadsheetApp.getActive().getSheetByName(SHEET_NAME);
  if (!sh) { Logger.log('STOP: no tab named ' + SHEET_NAME); return; }

  const rows = sh.getDataRange().getValues();
  const head = rows[0].map(function(h){ return String(h).trim(); });
  const rawHead = rows[0].map(String);

  var need = {}, nice = {};
  for (var k in NEED) {
    need[k] = head.indexOf(NEED[k]);
    if (need[k] === -1) { Logger.log('STOP: column not found: ' + NEED[k]); return; }
  }
  for (var k2 in NICE) {
    nice[k2] = head.indexOf(NICE[k2].trim());
    if (nice[k2] === -1) nice[k2] = rawHead.indexOf(NICE[k2]);
  }

  Logger.log('optional columns found: ' +
    (Object.keys(NICE).filter(function(x){ return nice[x] !== -1; }).join(', ') || 'none'));

  function cell(r, i) { return i === -1 ? '' : r[i]; }

  var events = [], mark = [], counts = {}, tooOld = 0, noKey = 0, unchanged = 0, withId = 0;

  for (var i = 1; i < rows.length; i++) {
    var r = rows[i];

    var stage = classify(r[need.booked], r[need.pabau]);
    if (!stage) {
      // No outcome yet. Still send the raw Lead stage once, Meta requires it.
      if (cell(r, nice.leadId)) stage = 'Lead'; else continue;
    }

    var last = String(r[need.stage] || '').trim();
    if (last === stage) { unchanged++; continue; }
    if (last && STAGE_RANK[last] && STAGE_RANK[stage] &&
        STAGE_RANK[stage] <= STAGE_RANK[last]) { unchanged++; continue; }

    var ud = buildUserData(
      cell(r, nice.leadId),
      cell(r, nice.leadEmail) || cell(r, nice.pabauEmail),
      cell(r, nice.leadPhone) || cell(r, nice.pabauPhone),
      r[need.name]
    );
    if (!ud) { noKey++; continue; }
    if (ud.lead_id) withId++;

    var when = stageTime(stage, r, need, nice);
    var ageDays = (Date.now() - when.getTime()) / 86400000;
    if (ageDays > MAX_AGE_DAYS) { tooOld++; continue; }
    if (ageDays < 0) when = new Date();

    events.push({
      event_name    : stage,
      event_time    : Math.floor(when.getTime() / 1000),
      action_source : 'system_generated',
      custom_data   : { event_source: 'crm', lead_event_source: CRM_NAME },
      user_data     : ud
    });
    mark.push({ row: i + 1, stage: stage });
    counts[stage] = (counts[stage] || 0) + 1;
  }

  Logger.log('to send: ' + events.length + '  ' + JSON.stringify(counts) +
             ' | with lead_id: ' + withId +
             ' | stage unchanged: ' + unchanged +
             ' | no identity: ' + noKey +
             ' | older than ' + MAX_AGE_DAYS + ' days: ' + tooOld);

  if (DRY_RUN) {
    Logger.log('DRY RUN, nothing sent. Sample: ' + JSON.stringify(events.slice(0, 2), null, 2));
    return;
  }

  var sentOk = 0;
  for (var j = 0; j < events.length; j += 100) {
    var body = { data: events.slice(j, j + 100), access_token: token };
    if (TEST_EVENT_CODE) body.test_event_code = TEST_EVENT_CODE;

    var res = UrlFetchApp.fetch(
      'https://graph.facebook.com/' + API_VERSION + '/' + DATASET_ID + '/events',
      { method:'post', contentType:'application/json',
        muteHttpExceptions:true, payload: JSON.stringify(body) });

    Logger.log('batch ' + (j/100 + 1) + ' -> ' + res.getResponseCode() + ' ' + res.getContentText());

    if (res.getResponseCode() === 200) {
      var slice = mark.slice(j, j + 100);
      for (var m = 0; m < slice.length; m++) {
        sh.getRange(slice[m].row, need.stage + 1).setValue(slice[m].stage);
      }
      sentOk += slice.length;
    } else {
      Logger.log('batch failed, rows NOT marked, they retry next run');
    }
  }
  Logger.log('DONE. sent and marked: ' + sentOk);
}

/**** WHICH STAGE IS THIS ROW IN ****/
function classify(booked, pabau) {
  var b = String(booked || '').trim().toLowerCase();
  var p = String(pabau  || '').trim().toLowerCase();
  if (p === 'complete' || p === 'arrived' || p === 'running late') return 'ShowedUp';
  if (p === 'no show'  || p === 'not show')                        return 'NoShow';
  if (b === 'booked')                                              return 'ScheduledAppointment';
  if (b === 'not interested')                                      return 'Disqualified';
  return null;   // caller falls back to the raw Lead stage
}

/**** WHEN DID THIS STAGE HAPPEN ****/
function stageTime(stage, r, need, nice) {
  if (stage === 'ShowedUp' || stage === 'NoShow') {
    var t = r[need.updated] ? new Date(r[need.updated]) : null;
    if (t && !isNaN(t.getTime())) return t;
  }
  if (stage === 'Lead' && nice.leadDate !== -1) {
    var d = r[nice.leadDate] ? new Date(r[nice.leadDate]) : null;
    if (d && !isNaN(d.getTime())) return d;
  }
  return new Date();   // detected this hour
}

/**** IDENTITY: lead_id first, hashed details alongside ****/
function buildUserData(leadId, email, phone, fullName) {
  var id = String(leadId == null ? '' : leadId).replace(/[^0-9]/g, '');
  var em = sha256(normEmail(email));
  var ph = sha256(normPhone(phone));
  if (!id && !em && !ph) return null;

  var ud = { country: [sha256(COUNTRY)] };
  if (id) ud.lead_id = id;   // string, exactly as Meta's own Explorer sends it
  if (em) ud.em = [em];
  if (ph) ud.ph = [ph];

  var n  = splitName(fullName);
  var fn = sha256(normName(n.fn)); if (fn) ud.fn = [fn];
  var ln = sha256(normName(n.ln)); if (ln) ud.ln = [ln];
  return ud;
}

function sha256(s) {
  if (!s) return null;
  var bytes = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, s, Utilities.Charset.UTF_8);
  var out = '';
  for (var i = 0; i < bytes.length; i++) {
    out += ('0' + (bytes[i] & 0xFF).toString(16)).slice(-2);
  }
  return out;
}

function normEmail(v){ return String(v == null ? '' : v).trim().toLowerCase(); }

function normPhone(v){
  var d = String(v == null ? '' : v).replace(/[^0-9]/g, '');
  if (!d) return '';
  if (d.charAt(0) === '0') d = '92' + d.substring(1);
  return d;
}

function normName(v){
  return String(v == null ? '' : v).trim().toLowerCase().replace(/[^a-z]/g, '');
}

function splitName(full){
  var p = String(full == null ? '' : full).trim().split(/\s+/).filter(Boolean);
  if (!p.length) return { fn:'', ln:'' };
  return { fn: p[0], ln: p.length > 1 ? p[p.length - 1] : '' };
}

/**** ---- TEST-ONLY HELPERS. Delete these before you use this on a real sheet. ---- ****/

// A fake person. Nothing here belongs to a real customer.
var TEST_LEAD_ID = '9001000000000001';
var TEST_EMAIL   = 'ayesha.khan@example.com';
var TEST_PHONE   = '+92300-1111111';
var TEST_NAME    = 'Ayesha Khan';

/**** 1. Does the token work at all? Sends ONE event. ****/
function sendTestEvent() {
  var token = PropertiesService.getScriptProperties().getProperty('META_TOKEN');
  if (!token) { Logger.log('STOP: META_TOKEN not set. See Step 12.'); return; }

  var body = {
    data: [{
      event_name    : 'ShowedUp',
      event_time    : Math.floor(Date.now() / 1000),
      action_source : 'system_generated',
      custom_data   : { event_source: 'crm', lead_event_source: CRM_NAME },
      user_data     : buildUserData(TEST_LEAD_ID, TEST_EMAIL, TEST_PHONE, TEST_NAME)
    }],
    access_token: token
  };
  if (TEST_EVENT_CODE) body.test_event_code = TEST_EVENT_CODE;

  var res = UrlFetchApp.fetch(
    'https://graph.facebook.com/' + API_VERSION + '/' + DATASET_ID + '/events',
    { method:'post', contentType:'application/json',
      muteHttpExceptions:true, payload: JSON.stringify(body) });

  Logger.log(res.getResponseCode() + ' ' + res.getContentText());
}

/**** 2. Sends the whole ladder for one fake lead, a minute apart, in order. ****/
function sendFullLadderForTestLead() {
  var token = PropertiesService.getScriptProperties().getProperty('META_TOKEN');
  if (!token) { Logger.log('STOP: META_TOKEN not set. See Step 12.'); return; }

  var ud = buildUserData(TEST_LEAD_ID, TEST_EMAIL, TEST_PHONE, TEST_NAME);
  var now = Math.floor(Date.now() / 1000);
  var ladder = ['Lead', 'ScheduledAppointment', 'ShowedUp'];
  var data = [];

  for (var i = 0; i < ladder.length; i++) {
    data.push({
      event_name    : ladder[i],
      event_time    : now - (ladder.length - i) * 60,
      action_source : 'system_generated',
      custom_data   : { event_source: 'crm', lead_event_source: CRM_NAME },
      user_data     : ud
    });
  }

  var body = { data: data, access_token: token };
  if (TEST_EVENT_CODE) body.test_event_code = TEST_EVENT_CODE;

  var res = UrlFetchApp.fetch(
    'https://graph.facebook.com/' + API_VERSION + '/' + DATASET_ID + '/events',
    { method:'post', contentType:'application/json',
      muteHttpExceptions:true, payload: JSON.stringify(body) });

  Logger.log(res.getResponseCode() + ' ' + res.getContentText());
}

/**** 3. Prints the hash of one value, so you can compare it to Meta's own hash. ****/
function showHashes() {
  Logger.log('email  ' + TEST_EMAIL + '  ->  ' + sha256(normEmail(TEST_EMAIL)));
  Logger.log('phone  ' + TEST_PHONE + '  ->  ' + sha256(normPhone(TEST_PHONE)));
  Logger.log('country pk ->  ' + sha256('pk'));
}

/**** 4. Moves the demo dates so nothing is older than 7 days. Run this if the sheet
        has been sitting for a while and rows start getting skipped as too old. ****/
function refreshDemoDates() {
  var sh = SpreadsheetApp.getActive().getSheetByName(SHEET_NAME);
  if (!sh) { Logger.log('STOP: no tab named ' + SHEET_NAME); return; }

  var rows = sh.getDataRange().getValues();
  var head = rows[0].map(function(h){ return String(h).trim(); });
  var cDate = head.indexOf('Date');
  var cUpd  = head.indexOf('CONSULATION STATUS UPDATED AT');
  var cName = head.indexOf('Full Name');
  if (cDate === -1 || cUpd === -1 || cName === -1) { Logger.log('STOP: columns missing'); return; }

  // name -> [days ago for Date, days ago for updated or null]
  var PLAN = {
    'Ayesha Khan':[1,null], 'Bilal Ahmed':[1,null], 'Sana Malik':[2,null],
    'Usman Tariq':[3,null], 'Hina Raza':[3,1], 'Omar Sheikh':[4,2],
    'Zara Iqbal':[4,2], 'Kamran Butt':[5,null], 'Nadia Aslam':[2,null],
    'Faisal Qureshi':[3,1], 'Rabia Noor':[3,1], 'Old Record':[20,20]
  };

  function stamp(daysAgo) {
    var d = new Date();
    d.setDate(d.getDate() - daysAgo);
    return Utilities.formatDate(d, Session.getScriptTimeZone(), 'yyyy-MM-dd HH:mm:ss');
  }

  var n = 0;
  for (var i = 1; i < rows.length; i++) {
    var p = PLAN[String(rows[i][cName]).trim()];
    if (!p) continue;
    sh.getRange(i + 1, cDate + 1).setValue(stamp(p[0]));
    if (p[1] !== null) sh.getRange(i + 1, cUpd + 1).setValue(stamp(p[1]));
    n++;
  }
  Logger.log('refreshed ' + n + ' rows');
}
