/* PRODUCTION-DAY COUNT REFRESH  (9 profiles)
   Re-reads every Venus Google Business Profile, prints the live total, and
   rewrites data.js with the new counts, ratings and today's date.

   Usage:   node refresh-counts.js            (headless)
            node refresh-counts.js headful    (Google sometimes serves headless
                                               Chrome a degraded page - notably
                                               MM Alam and Lake City)

   Then re-render:
            node capture.js full        (~13 min, 1350 frames)
            node verify.js              (confirms no text overflows anywhere)
            python cover.py
            ffmpeg -y -framerate 30 -start_number 0 -i frames/%05d.png \
              -i Venus_Reel_Soundtrack_48k.wav -c:v libx264 -preset slow -crf 17 \
              -pix_fmt yuv420p -profile:v high -c:a aac -b:a 192k -ar 48000 \
              -movflags +faststart -shortest OUT.mp4

   Partial re-render (much faster when only one section changed):
            node capture.js range <startFrame> <endFrame>
*/
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const sleep = ms => new Promise(r => setTimeout(r, ms));

const P = [
  { id: '01', q: 'Venus Aesthetics MM Alam Rd Lahore' },
  { id: '02', q: 'Venus Aesthetics DHA Phase 5 Lahore' },
  { id: '03', q: 'Venus Aesthetics Faisal Town Lahore' },
  { id: '04', q: 'Venus Aesthetics Lake City Lahore' },
  { id: '05', q: 'Venus Aesthetics F-7 Markaz Islamabad' },
  { id: '06', q: 'Venus Aesthetics D Ground Faisalabad' },
  { id: '07', q: 'Venus Aesthetics Gujranwala' },
  { id: '08', q: 'Venus Aesthetics Karachi Shaheed-e-Millat Rd' },
  { id: '09', q: 'Venus Aesthetics DHA Phase 6 Karachi' },
];

(async () => {
  const headful = process.argv[2] === 'headful';
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: headful ? false : 'new',
    args: ['--no-sandbox', '--lang=en-US', '--window-size=1250,1050'],
    defaultViewport: { width: 1250, height: 1050, deviceScaleFactor: 2 },
  });

  const out = [];
  for (const p of P) {
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36');
    await page.goto(`https://www.google.com/maps/search/${encodeURIComponent(p.q)}?hl=en&gl=us`,
      { waitUntil: 'networkidle2', timeout: 120000 });

    let hit = null;
    for (let k = 0; k < 26; k++) {
      hit = await page.evaluate(() => {
        const e = document.querySelector('div.F7nice');
        if (e) {
          const m = e.innerText.replace(/\s+/g, ' ').match(/([\d.]+)\s*\(([\d,]+)\)/);
          if (m) return { rating: m[1], count: m[2] };
        }
        return null;
      });
      if (hit) break;
      await page.mouse.move(600 + k * 3, 500);
      await sleep(1500);
    }
    const meta = await page.evaluate(() => ({
      name: document.querySelector('h1')?.innerText.trim() || null,
      closed: /Permanently closed/i.test(document.body.innerText) ? 'PERMANENTLY_CLOSED' : null,
    }));
    out.push({ ...p, ...meta, ...(hit || { rating: null, count: null }) });
    console.log(`${p.id}  ${meta.name}  ${hit ? hit.rating + ' (' + hit.count + ')' : 'FAILED - rerun headful'} ${meta.closed || ''}`);
    await page.close();
  }
  await browser.close();

  const bad = out.filter(o => !o.count);
  if (bad.length) {
    console.log(`\n!! ${bad.length} profile(s) failed to read: ${bad.map(b => b.id).join(', ')}`);
    console.log('!! Re-run with: node refresh-counts.js headful');
    console.log('!! data.js was NOT modified - it never writes a partial total.');
    return;
  }

  const total = out.reduce((s, o) => s + parseInt(o.count.replace(/,/g, ''), 10), 0);
  console.log('\nLIVE NETWORK TOTAL = ' + total.toLocaleString());
  console.log(total >= 10000
    ? '>>> 10,000+ remains substantiated (margin +' + (total - 10000) + ')'
    : '>>> BELOW 10,000 by ' + (10000 - total) + ' - the 10,000+ claim must NOT be used');

  const dp = path.join(__dirname, 'data.js');
  let src = fs.readFileSync(dp, 'utf8');
  out.forEach(o => {
    const n = parseInt(o.count.replace(/,/g, ''), 10);
    src = src.replace(new RegExp(`(id:'${o.id}',[\\s\\S]*?count:)\\d+`), `$1${n}`);
    src = src.replace(new RegExp(`(id:'${o.id}',[\\s\\S]*?rating:')[\\d.]+`), `$1${o.rating}`);
  });
  const d = new Date();
  const stamp = `${d.getDate()} ${d.toLocaleString('en-US', { month: 'long' }).toUpperCase()} ${d.getFullYear()}`;
  src = src.replace(/CAPTURE_DATE = '[^']*'/, `CAPTURE_DATE = '${stamp}'`);
  fs.writeFileSync(dp, src);
  fs.writeFileSync(path.join(__dirname, 'last-refresh.json'),
    JSON.stringify({ capturedAt: d.toISOString(), total, branches: out }, null, 2));
  console.log('data.js updated to ' + stamp + '. Next: node capture.js full');
})();
