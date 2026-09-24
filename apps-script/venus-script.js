/**** ============================================================
      VENUS AESTHETICS  ·  outcome events back to Meta
      Reads your lead sheet, works out what stage each lead is at,
      and tells Meta. Runs every hour. Never sends the same thing twice.
      ============================================================ ****/

/**** CONFIG ****/
const DATASET_ID   = '726819547675464';
const API_VERSION  = 'v26.0';

// Every tab that holds leads. Run listTabs() once to get the exact names.
const SHEET_NAMES  = ['Islamabad Logic'];   // step 8 tells you what to put here

const DRY_RUN            = true;   // step 16 tells you when to change this
const TEST_EVENT_CODE    = '';     // leave empty, CRM events have no test code
const MAX_AGE_DAYS       = 7;      // Meta rejects events older than this
const MAX_EVENTS_PER_RUN = 2000;   // safety brake on the very first run
const COUNTRY            = 'pk';
const CRM_NAME           = 'Venus Lead Flow';

// Required columns. A tab missing any of these is skipped with a warning.
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
  leadDate  : ' Date',              // note the leading space
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

/**** ============ MAIN. This is what the hourly trigger runs. ============ ****/
function sendStagesToMeta() {
  var token = PropertiesService.getScriptProperties().getProperty('META_TOKEN');
  if (!token) { Logger.log('STOP: META_TOKEN not set. See step 7.'); return; }

  var ss = SpreadsheetApp.getActive();
  var books = [];      // one entry per usable tab
  var queue = [];      // flat list of everything to send, across all tabs
  var total = { counts:{}, withId:0, unchanged:0, noKey:0, tooOld:0, noStageCol:0 };

  for (var t = 0; t < SHEET_NAMES.length; t++) {
    var sh = ss.getSheetByName(SHEET_NAMES[t]);
    if (!sh) { Logger.log('WARN: no tab named ' + SHEET_NAMES[t] + ', skipped'); continue; }

    var book = scanTab(sh, total, queue, books.length);
    if (book) books.push(book);
  }

  if (!books.length) { Logger.log('STOP: no usable tab found. Run listTabs().'); return; }

  var capped = false;
  if (queue.length > MAX_EVENTS_PER_RUN) {
    queue = queue.slice(0, MAX_EVENTS_PER_RUN);
    capped = true;
  }

  Logger.log('to send: ' + queue.length + '  ' + JSON.stringify(total.counts) +
             ' | with lead_id: ' + total.withId +
             ' | stage unchanged: ' + total.unchanged +
             ' | no identity: ' + total.noKey +
             ' | older than ' + MAX_AGE_DAYS + ' days: ' + total.tooOld +
             (capped ? '  [CAPPED at ' + MAX_EVENTS_PER_RUN + ', rest goes next run]' : ''));

  if (DRY_RUN) {
    Logger.log('DRY RUN, nothing sent. Sample: ' +
      JSON.stringify(queue.slice(0, 2).map(function(q){ return q.ev; }), null, 2));
    return;
  }

  var sentOk = 0;
  for (var j = 0; j < queue.length; j += 100) {
    var slice = queue.slice(j, j + 100);
    var body  = { data: slice.map(function(q){ return q.ev; }), access_token: token };
    if (TEST_EVENT_CODE) body.test_event_code = TEST_EVENT_CODE;

    var res = UrlFetchApp.fetch(
      'https://graph.facebook.com/' + API_VERSION + '/' + DATASET_ID + '/events',
      { method:'post', contentType:'application/json',
        muteHttpExceptions:true, payload: JSON.stringify(body) });

    var code = res.getResponseCode();
    Logger.log('batch ' + (j/100 + 1) + ' -> ' + code + ' ' + res.getContentText());

    if (code !== 200) { Logger.log('batch failed, rows NOT marked, they retry next run'); continue; }

    // mark in memory, then write each touched tab's column in ONE call
    var touched = {};
    for (var m = 0; m < slice.length; m++) {
      var q = slice[m];
      books[q.book].col[q.line][0] = q.stage;
      touched[q.book] = true;
    }
    for (var b in touched) flushTab(books[b]);
    sentOk += slice.length;
  }
  Logger.log('DONE. sent and marked: ' + sentOk);
}

/**** read one tab, push its work onto the queue ****/
function scanTab(sh, total, queue, bookIndex) {
  var rows = sh.getDataRange().getValues();
  if (rows.length < 2) return null;

  var head    = rows[0].map(function(h){ return String(h).trim(); });
  var rawHead = rows[0].map(String);

  var need = {}, nice = {}, missing = [];
  for (var k in NEED) {
    need[k] = head.indexOf(NEED[k]);
    if (need[k] === -1) missing.push(NEED[k]);
  }
  if (missing.length) {
    Logger.log('WARN: ' + sh.getName() + ' skipped, missing column: ' + missing.join(', '));
    if (missing.indexOf(NEED.stage) !== -1) total.noStageCol++;
    return null;
  }
  for (var k2 in NICE) {
    nice[k2] = head.indexOf(NICE[k2].trim());
    if (nice[k2] === -1) nice[k2] = rawHead.indexOf(NICE[k2]);
  }

  Logger.log(sh.getName() + ': ' + (rows.length - 1) + ' rows, optional columns found: ' +
    (Object.keys(NICE).filter(function(x){ return nice[x] !== -1; }).join(', ') || 'none'));

  function cell(r, i) { return i === -1 ? '' : r[i]; }

  var book = {
    sh: sh,
    stageColIdx: need.stage,
    col: rows.slice(1).map(function(r){ return [String(r[need.stage] == null ? '' : r[need.stage])]; })
  };

  for (var i = 1; i < rows.length; i++) {
    var r = rows[i];

    var stage = classify(r[need.booked], r[need.pabau]);
    if (!stage) {
      if (cell(r, nice.leadId)) stage = 'Lead'; else continue;
    }

    var last = String(r[need.stage] || '').trim();
    if (last === stage) { total.unchanged++; continue; }
    if (last && STAGE_RANK[last] && STAGE_RANK[stage] &&
        STAGE_RANK[stage] <= STAGE_RANK[last]) { total.unchanged++; continue; }

    var ud = buildUserData(
      cell(r, nice.leadId),
      cell(r, nice.leadEmail) || cell(r, nice.pabauEmail),
      cell(r, nice.leadPhone) || cell(r, nice.pabauPhone),
      r[need.name]
    );
    if (!ud) { total.noKey++; continue; }

    var when = stageTime(stage, r, need, nice);
    var ageDays = (Date.now() - when.getTime()) / 86400000;
    if (ageDays > MAX_AGE_DAYS) { total.tooOld++; continue; }
    if (ageDays < 0) when = new Date();

    if (ud.lead_id) total.withId++;
    total.counts[stage] = (total.counts[stage] || 0) + 1;

    queue.push({
      book : bookIndex,
      line : i - 1,          // index into book.col
      stage: stage,
      ev   : {
        event_name    : stage,
        event_time    : Math.floor(when.getTime() / 1000),
        action_source : 'system_generated',
        custom_data   : { event_source: 'crm', lead_event_source: CRM_NAME },
        user_data     : ud
      }
    });
  }

  return book;
}

/**** write one tab's whole stage column in a single call ****/
function flushTab(book) {
  if (!book.col.length) return;
  book.sh.getRange(2, book.stageColIdx + 1, book.col.length, 1).setValues(book.col);
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
  return new Date();
}

/**** IDENTITY: lead_id first, hashed details alongside ****/
function buildUserData(leadId, email, phone, fullName) {
  var id = String(leadId == null ? '' : leadId).replace(/[^0-9]/g, '');
  var em = sha256(normEmail(email));
  var ph = sha256(normPhone(phone));
  if (!id && !em && !ph) return null;

  var ud = { country: [sha256(COUNTRY)] };
  if (id) ud.lead_id = id;   // string, unhashed, exactly as Meta expects
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

/**** ============ SETUP HELPERS. Run these by hand, once. ============ ****/

/**** Lists every tab, its row count, and whether it is ready to use.
      Copy the ready ones into SHEET_NAMES at the top. ****/
function listTabs() {
  var shs = SpreadsheetApp.getActive().getSheets();
  for (var i = 0; i < shs.length; i++) {
    var sh = shs[i];
    if (sh.getLastColumn() < 1 || sh.getLastRow() < 1) {
      Logger.log('"' + sh.getName() + '"  empty'); continue;
    }
    var head = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]
                 .map(function(h){ return String(h).trim(); });
    var missing = [];
    for (var k in NEED) if (head.indexOf(NEED[k]) === -1) missing.push(NEED[k]);
    Logger.log('"' + sh.getName() + '"  rows: ' + (sh.getLastRow() - 1) + '  ' +
      (missing.length ? 'MISSING -> ' + missing.join(' | ') : 'READY'));
  }
}

/**** Adds the "Meta Stage Sent" header to every tab that already has the
      other four required columns. Adds a header only. Touches no data. ****/
function addStageColumnEverywhere() {
  var shs = SpreadsheetApp.getActive().getSheets();
  var added = 0;
  for (var i = 0; i < shs.length; i++) {
    var sh = shs[i];
    if (sh.getLastColumn() < 1 || sh.getLastRow() < 1) continue;
    var head = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]
                 .map(function(h){ return String(h).trim(); });
    if (head.indexOf(NEED.stage) !== -1) { Logger.log('"' + sh.getName() + '" already has it'); continue; }

    var others = [NEED.booked, NEED.pabau, NEED.updated, NEED.name]
                   .filter(function(c){ return head.indexOf(c) === -1; });
    if (others.length) { Logger.log('"' + sh.getName() + '" not a lead tab, left alone'); continue; }

    sh.getRange(1, sh.getLastColumn() + 1).setValue(NEED.stage);
    Logger.log('"' + sh.getName() + '" -> added in column ' + (sh.getLastColumn()));
    added++;
  }
  Logger.log('tabs updated: ' + added);
}

/**** Sends ONE event so you can confirm the token works.
      Uses a lead id that exists in your sheet, so it is a real check. ****/
function sendOneRealEvent() {
  var token = PropertiesService.getScriptProperties().getProperty('META_TOKEN');
  if (!token) { Logger.log('STOP: META_TOKEN not set.'); return; }

  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName(SHEET_NAMES[0]);
  if (!sh) { Logger.log('STOP: no tab named ' + SHEET_NAMES[0]); return; }

  var rows = sh.getDataRange().getValues();
  var head = rows[0].map(function(h){ return String(h).trim(); });
  var cId  = head.indexOf(NICE.leadId);
  var cEm  = head.indexOf(NICE.leadEmail);
  var cPh  = head.indexOf(NICE.leadPhone);
  var cNm  = head.indexOf(NEED.name);
  if (cId === -1) { Logger.log('STOP: no ' + NICE.leadId + ' column'); return; }

  var pick = null;
  for (var i = rows.length - 1; i > 0; i--) {
    if (String(rows[i][cId] || '').replace(/[^0-9]/g, '')) { pick = rows[i]; break; }
  }
  if (!pick) { Logger.log('STOP: no row with a lead id'); return; }

  var ud = buildUserData(pick[cId], cEm === -1 ? '' : pick[cEm],
                         cPh === -1 ? '' : pick[cPh], cNm === -1 ? '' : pick[cNm]);
  Logger.log('using lead_id ' + ud.lead_id);

  var body = {
    data: [{
      event_name    : 'Lead',
      event_time    : Math.floor(Date.now() / 1000),
      action_source : 'system_generated',
      custom_data   : { event_source: 'crm', lead_event_source: CRM_NAME },
      user_data     : ud
    }],
    access_token: token
  };

  var res = UrlFetchApp.fetch(
    'https://graph.facebook.com/' + API_VERSION + '/' + DATASET_ID + '/events',
    { method:'post', contentType:'application/json',
      muteHttpExceptions:true, payload: JSON.stringify(body) });

  Logger.log(res.getResponseCode() + ' ' + res.getContentText());
}
