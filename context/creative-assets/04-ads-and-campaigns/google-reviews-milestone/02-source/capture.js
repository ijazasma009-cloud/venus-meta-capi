const puppeteer=require('puppeteer-core');
const http=require('http'), fs=require('fs'), path=require('path');
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const ROOT=__dirname;
const MIME={'.html':'text/html','.js':'text/javascript','.jpg':'image/jpeg','.png':'image/png','.ttf':'font/ttf'};

const MODE=process.argv[2]||'preview';
let RANGE_START=0;
const OUT=path.join(ROOT, (MODE==='full'||MODE==='range')?'frames':'preview');
fs.mkdirSync(OUT,{recursive:true});

const srv=http.createServer((rq,rs)=>{
  let p=path.join(ROOT, decodeURIComponent(rq.url.split('?')[0]));
  if(rq.url==='/'||rq.url==='') p=path.join(ROOT,'index.html');
  if(!fs.existsSync(p)){rs.writeHead(404);return rs.end();}
  rs.writeHead(200,{'Content-Type':MIME[path.extname(p)]||'application/octet-stream'});
  fs.createReadStream(p).pipe(rs);
});

(async()=>{
  await new Promise(r=>srv.listen(8731,r));
  const browser=await puppeteer.launch({executablePath:CHROME,headless:'new',
    args:['--no-sandbox','--force-device-scale-factor=1','--hide-scrollbars','--font-render-hinting=none','--disable-lcd-text'],
    defaultViewport:{width:1080,height:1920,deviceScaleFactor:1}});
  const page=await browser.newPage();
  page.on('pageerror',e=>console.log('PAGEERROR:',e.message));
  page.on('console',m=>{ if(m.type()==='error') console.log('CONSOLE:',m.text()); });
  await page.goto('http://127.0.0.1:8731/index.html',{waitUntil:'networkidle0',timeout:60000});
  await page.waitForFunction('window.READY===true',{timeout:120000});
  console.log('renderer ready');

  const el=await page.$('#c');
  let times=[];
  if(MODE==='full'){ for(let f=0;f<45*30;f++) times.push(f/30); }
  else if(MODE==='range'){
    const a=parseInt(process.argv[3],10), b=parseInt(process.argv[4],10);
    for(let f=a; f<=b; f++) times.push(f/30);
    RANGE_START=a;
  }
  else times=[0.9, 1.8, 2.6, 3.6, 5.0, 6.4, 7.0, 7.6, 8.3, 8.9, 10.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0, 25.0, 26.2, 27.2, 28.2, 28.6, 29.0, 29.4, 29.7, 30.0, 30.6, 31.4, 32.3, 33.2, 34.2, 35.2, 36.0, 36.4, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 42.6, 43.1, 43.6, 44.2, 44.8];
  const t0=Date.now();
  for(let i=0;i<times.length;i++){
    await page.evaluate(t=>window.seek(t),times[i]);
    const name = MODE==='full' ? String(i).padStart(5,'0')
               : MODE==='range' ? String(RANGE_START+i).padStart(5,'0')
               : times[i].toFixed(2).replace('.','_');
    await el.screenshot({path:path.join(OUT,name+'.png')});
    if((MODE==='full'||MODE==='range')&&i%40===0){
      const el2=(Date.now()-t0)/1000, eta=el2/(i+1)*(times.length-i-1);
      console.log(`frame ${i}/${times.length}  ${el2.toFixed(0)}s elapsed  ETA ${eta.toFixed(0)}s`);
    }
  }
  console.log('captured',times.length,'frames in',((Date.now()-t0)/1000).toFixed(0)+'s');
  await browser.close(); srv.close();
})();
