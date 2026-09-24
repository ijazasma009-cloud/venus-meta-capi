// Regenerates demo/demo-sheet.csv with dates relative to today, so the rows are
// inside Meta's 7-day window whenever you build the sandbox sheet.
//
//   node tools/make-demo-sheet.cjs
//
// Twelve rows, each one there to trip a different branch:
//   2 raw leads, 2 booked, 3 arrivals, 1 no-show, 1 disqualified,
//   1 with no identity at all, 1 already at the top of the ladder,
//   1 mid-ladder that must climb, 1 too old to send.
// Expected dry run: to send: 9, skipped 3.
const fs = require('fs'), path = require('path');

const D = n => { const d = new Date(); d.setDate(d.getDate() - n); return d; };
const iso = d => { const p = x => String(x).padStart(2, '0');
  return d.getFullYear() + '-' + p(d.getMonth()+1) + '-' + p(d.getDate()) + ' ' +
         p(d.getHours()) + ':' + p(d.getMinutes()) + ':' + p(d.getSeconds()); };

const HEAD = [' Date','Full Name','Booked Status','Pabau Status','CONSULATION STATUS UPDATED AT',
              'Meta Lead ID','Lead Phone','Lead Email','Pabau Client Mobile','Pabau Client Email','Meta Stage Sent'];

const ROWS = [
 [iso(D(1)),'Ayesha Khan','No Contact','','','9001000000000001','+92300-1111111','ayesha.khan@example.com','','',''],
 [iso(D(1)),'Bilal Ahmed','Call Later','','','9001000000000002','+92301-2222222','bilal.ahmed@example.com','','',''],
 [iso(D(2)),'Sana Malik','Booked','','','9001000000000003','+92302-3333333','sana.malik@example.com','','',''],
 [iso(D(3)),'Usman Tariq','Booked','Waiting','','9001000000000004','+92303-4444444','usman.tariq@example.com','','',''],
 [iso(D(3)),'Hina Raza','Booked','Complete',iso(D(1)),'9001000000000005','+92304-5555555','hina.raza@example.com','+92304-5555555','hina.raza@example.com',''],
 [iso(D(4)),'Omar Sheikh','Booked','Arrived',iso(D(2)),'9001000000000006','+92305-6666666','omar.sheikh@example.com','+92305-6666666','omar.sheikh@example.com',''],
 [iso(D(4)),'Zara Iqbal','Booked','No Show',iso(D(2)),'9001000000000007','+92306-7777777','zara.iqbal@example.com','+92306-7777777','zara.iqbal@example.com',''],
 [iso(D(5)),'Kamran Butt','Not Interested','','','9001000000000008','+92307-8888888','kamran.butt@example.com','','',''],
 [iso(D(2)),'Nadia Aslam','Booked','','','','','','','',''],                        // no identity, must skip
 [iso(D(3)),'Faisal Qureshi','Booked','Complete',iso(D(1)),'9001000000000010','+92309-9999999','faisal.q@example.com','','','ShowedUp'],             // already top, must skip
 [iso(D(3)),'Rabia Noor','Booked','Complete',iso(D(1)),'9001000000000011','+92310-1010101','rabia.noor@example.com','','','ScheduledAppointment'],   // must climb
 [iso(D(20)),'Old Record','Booked','Complete',iso(D(20)),'9001000000000012','+92311-1111000','old.record@example.com','','',''],                     // too old, must skip
];

const esc = v => /[",\n]/.test(v) ? '"' + String(v).replace(/"/g, '""') + '"' : v;
const out = path.join(__dirname, '..', 'demo', 'demo-sheet.csv');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, [HEAD, ...ROWS].map(r => r.map(esc).join(',')).join('\n') + '\n', 'utf8');
console.log('wrote ' + out + ', ' + ROWS.length + ' data rows');
