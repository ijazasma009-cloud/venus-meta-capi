const puppeteer=require('puppeteer-core'); const http=require('http'),fs=require('fs'),path=require('path');
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const MIME={'.html':'text/html','.js':'text/javascript','.jpg':'image/jpeg','.png':'image/png','.ttf':'font/ttf'};
const srv=http.createServer((rq,rs)=>{let p=path.join(__dirname,decodeURIComponent(rq.url.split('?')[0]));
 if(rq.url==='/')p=path.join(__dirname,'index.html');
 if(!fs.existsSync(p)){rs.writeHead(404);return rs.end();}
 rs.writeHead(200,{'Content-Type':MIME[path.extname(p)]||'application/octet-stream'});fs.createReadStream(p).pipe(rs);});
(async()=>{
 await new Promise(r=>srv.listen(8734,r));
 const b=await puppeteer.launch({executablePath:CHROME,headless:'new',args:['--no-sandbox'],defaultViewport:{width:1080,height:1920}});
 const pg=await b.newPage();
 pg.on('console',m=>{ if(/sizes|particles/.test(m.text())) console.log('PAGE:',m.text()); });
 await pg.goto('http://127.0.0.1:8734/index.html',{waitUntil:'networkidle0'});
 await pg.waitForFunction('window.READY===true',{timeout:120000});
 const R=await pg.evaluate(()=>{
  const g=document.getElementById('c').getContext('2d');
  const tw=(t,sp=0)=>{let w=0;for(const c of [...t])w+=g.measureText(c).width+sp;return w-sp;};
  const out=[]; const SAFE=1080-110;
  const chk=(l,font,txt,sp,lim)=>{g.font=font;const w=sp?tw(txt,sp):g.measureText(txt).width;out.push({l,w:Math.round(w),lim,over:w>lim});};
  chk('B word',`300 ${SZ.bWord}px Cormorant`,'ONE EXPERIENCE.',0,SAFE);
  chk('C line2',`300 ${SZ.cLine}px Cormorant`,'NEVER BUILT IN ONE PLACE.',0,SAFE);
  chk('counter',`800 ${SZ.counter}px Archivo`,nfmt(TOTAL),0,1080-130);
  chk('still',`400 italic ${SZ.still}px Cormorant`,'AND WE’RE STILL COUNTING.',0,SAFE);
  chk('G line1',`300 ${SZ.gLine}px Cormorant`,'BEHIND EVERY REVIEW',0,SAFE);
  chk('thanks',`400 italic ${SZ.thanks}px Cormorant`,'THANK YOU, PAKISTAN.',0,SAFE);
  chk('H mark',`800 ${SZ.hMark}px Archivo`,MARK,0,SAFE);
  chk('H stmt',`500 ${SZ.hStmt}px Archivo`,'TIMES YOU CHOSE VENUS.',7,SAFE);
  chk('F mark',`800 ${SZ.fMark}px Archivo`,MARK,0,SAFE);
  // every branch name + rating row at render size
  for (const br of BRANCHES){
    let s=120; for(;s>40;s-=2){g.font=`800 ${s}px Archivo`; if(tw(br.name,3)<=1080-170)break;}
    g.font=`800 ${s}px Archivo`;
    out.push({l:'name '+br.id,w:Math.round(tw(br.name,3)),lim:1080-170,over:tw(br.name,3)>1080-170});
    g.font='600 36px Archivo';
    const rt=`${br.rating}   ·   +${br.count.toLocaleString()} GOOGLE REVIEWS`;
    const t=tw(rt,2.5), sw=(5-1)*32*1.34+32, tot=sw+40+t;
    out.push({l:'rate '+br.id,w:Math.round(tot),lim:1080-80,over:tot>1080-80});
  }
  return {out, SZ};
 });
 console.log('SIZES', JSON.stringify(R.SZ));
 let bad=0;
 R.out.forEach(r=>{ if(r.over) bad++; console.log((r.over?'!! OVER ':'   ok   ')+r.l.padEnd(12)+String(r.w).padStart(5)+' / '+r.lim); });
 console.log(bad? `\n${bad} OVERFLOW(S) REMAIN` : '\nALL TEXT FITS - no overflow anywhere');
 await b.close(); srv.close();
})();
