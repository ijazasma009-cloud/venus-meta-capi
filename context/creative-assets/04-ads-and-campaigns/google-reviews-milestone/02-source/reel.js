/* ==========================================================================
   VENUS AESTHETICS - "10,000 VOICES. ONE VENUS."
   v2 : slower pace, larger centred typography, smoother motion,
        9 branches, energetic counter apex on 10,000, treatment montage.
   Deterministic canvas renderer. seek(t) draws exactly one frame.
   ========================================================================== */
const W = 1080, H = 1920, FPS = 30, DUR = 45;
const C = {
  ink:'#08080A', ivory:'#F5F0E8', gold:'#C9A24B', goldHi:'#E8C874',
  star:'#F5B301', card:'#15151A'
};
const SERIF = 'Cormorant', SANS = 'Archivo';

const cv = document.getElementById('c');
const x  = cv.getContext('2d', { alpha:false });

/* ---------------- math / easing ---------------- */
const cl = (v,a=0,b=1) => v<a?a:v>b?b:v;
const lp = (a,b,t) => a+(b-a)*t;
const eOut   = t => 1-Math.pow(1-t,3);
const eOutQ  = t => 1-Math.pow(1-t,5);
const eIn    = t => t*t*t;
const eIO    = t => t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2;
const eIOQ   = t => t<.5 ? 16*t*t*t*t*t : 1-Math.pow(-2*t+2,5)/2;   // very smooth
const seg = (t,a,b) => cl((t-a)/(b-a));
function rnd(s){ const v = Math.sin(s*127.1+311.7)*43758.5453; return v-Math.floor(v); }
const nfmt = n => Math.round(n).toLocaleString('en-US');

/* ---------------- timeline (45.0s) ---------------- */
const T = {
  A:[0,3.0], B:[3.0,7.2], C:[7.2,8.6], D:[8.6,26.6],
  E:[26.6,31.0], F:[31.0,36.6], G:[36.6,42.2], H:[42.2,45.0]
};
const SLOT = 2.0;                    // seconds per branch (was 1.5 - slower)
const HANDOFF = 9940;                // counter value handed from D to E

/* ---------------- assets ---------------- */
const IMG = {};
async function loadAssets(){
  const names = [];
  for (let i=1;i<=9;i++) names.push('b'+String(i).padStart(2,'0'));
  for (let i=0;i<8;i++)  names.push('t'+i);
  await Promise.all(names.map(n => new Promise(res => {
    const im = new Image();
    im.onload = () => { IMG[n]=im; res(); };
    im.onerror = () => res();
    im.src = 'img/'+n+'.jpg';
  })));
  await new Promise(res => { const im=new Image(); im.onload=()=>{IMG.logo=im;res();}; im.src='img/logo.png'; });
}
async function loadFonts(){
  for (const [n,u] of [['Cormorant','fonts/CormorantGaramond.ttf'],
                       ['Archivo','fonts/Archivo.ttf'],
                       ['Inter','fonts/Inter.ttf']]) {
    const f = new FontFace(n, `url(${u})`, { weight:'100 900' });
    await f.load(); document.fonts.add(f);
  }
  await document.fonts.ready;
}

/* ---------------- text helpers ---------------- */
/* width of a tracked string */
function trackW(ctx, txt, sp){
  let w = 0; for (const c of [...txt]) w += ctx.measureText(c).width + sp;
  return w - sp;
}
/* draw tracked text; align is resolved here so canvas textAlign never matters */
function track(ctx, txt, cx, cy, sp, align='center'){
  const prev = ctx.textAlign; ctx.textAlign = 'left';
  const tot = trackW(ctx, txt, sp);
  let px = align==='center' ? cx-tot/2 : align==='right' ? cx-tot : cx;
  for (const c of [...txt]) { ctx.fillText(c, px, cy); px += ctx.measureText(c).width + sp; }
  ctx.textAlign = prev;
  return tot;
}
function wrap(ctx, txt, maxW){
  const words = txt.split(' '); const lines = []; let cur = '';
  for (const w of words){
    const t = cur ? cur+' '+w : w;
    if (ctx.measureText(t).width > maxW && cur) { lines.push(cur); cur = w; } else cur = t;
  }
  if (cur) lines.push(cur);
  return lines;
}
function rrect(ctx,X,Y,w,h,r){
  ctx.beginPath(); ctx.moveTo(X+r,Y);
  ctx.arcTo(X+w,Y,X+w,Y+h,r); ctx.arcTo(X+w,Y+h,X,Y+h,r);
  ctx.arcTo(X,Y+h,X,Y,r); ctx.arcTo(X,Y,X+w,Y,r); ctx.closePath();
}
function star1(ctx,cx,cy,r){
  ctx.beginPath();
  for (let i=0;i<10;i++){
    const a=-Math.PI/2+i*Math.PI/5, rr=i%2?r*0.45:r;
    const px=cx+Math.cos(a)*rr, py=cy+Math.sin(a)*rr;
    i?ctx.lineTo(px,py):ctx.moveTo(px,py);
  }
  ctx.closePath(); ctx.fill();
}
const starsW = (size,n=5) => (n-1)*size*1.34 + size;   // true visual width
function stars(ctx,leftX,cy,size,n=5,col=C.star){
  ctx.save(); ctx.fillStyle=col;
  const gap=size*1.34; let sx=leftX+size/2;
  for (let i=0;i<n;i++){ star1(ctx,sx,cy,size/2); sx+=gap; }
  ctx.restore();
}
function cover(ctx,im,X,Y,w,h,scale=1,ox=0,oy=0){
  if(!im) return;
  const tr=w/h, r=im.width/im.height;
  let sw,sh;
  if (r>tr){ sh=im.height; sw=sh*tr; } else { sw=im.width; sh=sw/tr; }
  sw/=scale; sh/=scale;
  const sx=(im.width-sw)/2 + ox*(im.width-sw)/2;
  const sy=(im.height-sh)/2 + oy*(im.height-sh)/2;
  ctx.drawImage(im,sx,sy,sw,sh,X,Y,w,h);
}
function vignette(ctx,s=0.75){
  const g=ctx.createRadialGradient(W/2,H*0.46,H*0.18,W/2,H*0.5,H*0.80);
  g.addColorStop(0,'rgba(0,0,0,0)'); g.addColorStop(1,`rgba(0,0,0,${s})`);
  ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
}
/* subtler, slower-moving grain so motion reads smoother */
function grain(ctx,t,amt=0.020){
  const n=90, s=Math.floor(t*FPS/2);
  ctx.save(); ctx.globalAlpha=amt;
  for (let i=0;i<n;i++){
    ctx.fillStyle = rnd(i+s)>0.5?'#fff':'#000';
    ctx.fillRect(rnd(s*7.13+i*3.77)*W, rnd(s*3.31+i*9.19)*H, 3,3);
  }
  ctx.restore();
}


/* largest px size at which txt fits maxW; guarantees nothing can overflow */
function fitPx(txt, weight, fam, start, maxW, sp=0){
  let px=start;
  for (; px>16; px-=1){
    x.font=`${weight} ${px}px ${fam}`;
    if (trackW(x,txt,sp) <= maxW) break;
  }
  return px;
}
const SAFE = W-110;          // horizontal safe area for display type
let SZ = {};
function buildSizes(){
  SZ.bWord = Math.min(
    fitPx('ONE EXPERIENCE.','300',SERIF,128,SAFE),
    fitPx('ONE STORY.','300',SERIF,128,SAFE),
    fitPx('ONE REVIEW.','300',SERIF,128,SAFE));
  SZ.cLine = Math.min(
    fitPx('BUT THIS STORY WAS','300',SERIF,96,SAFE),
    fitPx('NEVER BUILT IN ONE PLACE.','300',SERIF,96,SAFE));
  // one stable counter size for the widest value it will ever display
  SZ.counter = fitPx(nfmt(TOTAL),'800',SANS,310,W-130);
  SZ.still   = fitPx('AND WE’RE STILL COUNTING.','400 italic',SERIF,72,SAFE);
  SZ.gLine   = Math.min(
    fitPx('BEHIND EVERY REVIEW','300',SERIF,92,SAFE),
    fitPx('IS A STORY OF TRUST.','300',SERIF,92,SAFE));
  SZ.thanks  = fitPx('THANK YOU, PAKISTAN.','400 italic',SERIF,96,SAFE);
  SZ.hMark   = fitPx(MARK,'800',SANS,170,SAFE);
  SZ.hStmt   = fitPx('TIMES YOU CHOSE VENUS.','500',SANS,56,SAFE,7);
  SZ.fMark   = fitPx(MARK,'800',SANS,215,SAFE);
  // largest impact punch that keeps the widest counter value inside the frame
  x.font=`800 ${SZ.counter}px ${SANS}`;
  const cw = Math.max(x.measureText(nfmt(TOTAL)).width, x.measureText(nfmt(MILESTONE)).width);
  SZ.punch = Math.max(0, Math.min(0.17, (W-80)/cw - 1));
  PUNCH = SZ.punch;
  console.log('sizes',JSON.stringify(SZ));
}

/* ==========================================================================
   REVIEW CARDS - real Google review data, Venus-brand styling (larger)
   ========================================================================== */
const CW=720, CH=410;
const CARDS=[], ALLREV=[];
function buildCards(){
  BRANCHES.forEach(b => b.reviews.forEach(r => ALLREV.push({...r, br:b.name})));
  ALLREV.forEach(r => {
    const o=document.createElement('canvas'); o.width=CW; o.height=CH;
    const g=o.getContext('2d');
    g.fillStyle=C.card; rrect(g,0,0,CW,CH,30); g.fill();
    const grd=g.createLinearGradient(0,0,CW,CH);
    grd.addColorStop(0,'rgba(232,200,116,0.11)'); grd.addColorStop(0.55,'rgba(232,200,116,0.02)');
    grd.addColorStop(1,'rgba(232,200,116,0.08)');
    g.fillStyle=grd; rrect(g,0,0,CW,CH,30); g.fill();
    g.strokeStyle='rgba(201,162,75,0.32)'; g.lineWidth=2; rrect(g,1,1,CW-2,CH-2,30); g.stroke();
    // avatar
    const ax=60, ay=70, ar=36;
    const ag=g.createLinearGradient(ax-ar,ay-ar,ax+ar,ay+ar);
    ag.addColorStop(0,'#C9A24B'); ag.addColorStop(1,'#6B5220');
    g.fillStyle=ag; g.beginPath(); g.arc(ax,ay,ar,0,7); g.fill();
    g.fillStyle='#0C0C0E'; g.font=`600 34px ${SANS}`; g.textAlign='center'; g.textBaseline='middle';
    g.fillText((r.a||'V').trim()[0].toUpperCase(),ax,ay+1);
    g.textAlign='left'; g.textBaseline='alphabetic';
    let nm=r.a.trim(); if(nm.length>20) nm=nm.slice(0,19)+'…';
    g.fillStyle=C.ivory; g.font=`500 31px ${SANS}`; g.fillText(nm,114,64);
    g.fillStyle='rgba(245,240,232,0.44)'; g.font=`400 24px ${SANS}`; g.fillText(r.d,114,98);
    stars(g, CW-52-starsW(28), 68, 28, 5);
    g.fillStyle='rgba(245,240,232,0.92)'; g.font=`400 35px ${SERIF}`;
    wrap(g,'“'+r.t+'”',CW-116).slice(0,4).forEach((L,k)=>g.fillText(L,58,172+k*50));
    g.fillStyle='rgba(245,240,232,0.32)'; g.font=`500 19px ${SANS}`;
    track(g,'GOOGLE REVIEW',58,CH-34,3.4,'left');
    g.fillStyle='rgba(201,162,75,0.58)'; g.font=`500 19px ${SANS}`;
    track(g,r.br,CW-58,CH-34,3.4,'right');
    CARDS.push(o);
  });
}

/* ==========================================================================
   PARTICLES - "10,000+" mark and the Venus logo
   ========================================================================== */
function samplePoints(drawFn,w,h,step,maxN){
  const o=document.createElement('canvas'); o.width=w; o.height=h;
  const g=o.getContext('2d'); drawFn(g,w,h);
  const d=g.getImageData(0,0,w,h).data; const pts=[];
  for (let yy=0; yy<h; yy+=step) for (let xx=0; xx<w; xx+=step)
    if (d[(yy*w+xx)*4+3] > 130) pts.push({x:xx,y:yy});
  if (pts.length>maxN){
    const out=[], k=pts.length/maxN;
    for (let i=0;i<maxN;i++) out.push(pts[Math.floor(i*k)]);
    return out;
  }
  return pts;
}
const MARK = '10,000+';
const NUM_FONT=340, NUM_W=1900, NUM_H=560, LOGO_W=1200, LOGO_H=383;
let PARTS=[];
function buildParticles(){
  const NUMPTS = samplePoints((g,w,h)=>{
    g.clearRect(0,0,w,h); g.fillStyle='#fff';
    g.font=`800 ${NUM_FONT}px ${SANS}`; g.textAlign='center'; g.textBaseline='middle';
    g.fillText(MARK,w/2,h/2);
  }, NUM_W, NUM_H, 3, 5600);
  const LOGOPTS = samplePoints((g,w,h)=>{
    g.clearRect(0,0,w,h); g.drawImage(IMG.logo,0,0,w,h);
  }, LOGO_W, LOGO_H, 3, 5600);
  const N=Math.min(NUMPTS.length,LOGOPTS.length,4600);
  PARTS=[];
  for (let i=0;i<N;i++){
    const a=NUMPTS[Math.floor(i*NUMPTS.length/N)];
    const b=LOGOPTS[Math.floor(i*LOGOPTS.length/N)];
    const ang=rnd(i*1.7)*Math.PI*2, mag=150+Math.pow(rnd(i*3.1),0.55)*1000;
    PARTS.push({
      ax:a.x-NUM_W/2,  ay:a.y-NUM_H/2,
      bx:b.x-LOGO_W/2, by:b.y-LOGO_H/2,
      ex:Math.cos(ang)*mag, ey:Math.sin(ang)*mag*0.72,
      sd:rnd(i*5.3), sz:3.0+rnd(i*7.7)*3.2, dl:rnd(i*11.3)
    });
  }
  console.log('particles',PARTS.length);
}

/* ==========================================================================
   TUNNEL (A / B / C)
   ========================================================================== */
const NT=190, TUN=[];
function buildTunnel(){
  for (let i=0;i<NT;i++){
    const a=i*2.39996, r=(i===0)?0:(250+rnd(i*1.3)*590);
    TUN.push({
      x:Math.cos(a)*r, y:Math.sin(a)*r*1.22,
      z:(i===0)?3.0:(4.2+i*0.58+rnd(i*2.7)*0.55),
      ci:i%CARDS.length, rot:(rnd(i*4.1)-0.5)*0.24, br:0.55+rnd(i*6.9)*0.45
    });
  }
}
function drawTunnel(camZ, glow, alphaMul=1){
  const vis=[];
  for (const c of TUN){
    const dz=c.z-camZ;
    if (dz<0.55||dz>48) continue;
    vis.push({c,dz});
  }
  vis.sort((a,b)=>b.dz-a.dz);
  for (const {c,dz} of vis){
    const s=1/(dz/9.5);
    const a=cl((48-dz)/17)*cl(dz/1.5)*c.br*alphaMul;
    if (a<=0.004) continue;
    x.save(); x.globalAlpha=a;
    x.translate(W/2+c.x*s, H/2+c.y*s);
    x.rotate(c.rot*cl(dz/8)); x.scale(s*0.60,s*0.60);
    x.drawImage(CARDS[c.ci],-CW/2,-CH/2);
    x.restore();
  }
  if (glow>0){
    const g=x.createRadialGradient(W/2,H*0.5,0,W/2,H*0.5,780);
    g.addColorStop(0,`rgba(201,162,75,${0.16*glow})`); g.addColorStop(1,'rgba(201,162,75,0)');
    x.fillStyle=g; x.fillRect(0,0,W,H);
  }
}
const camZat = t => 78*Math.pow(cl((t-T.B[0])/(T.B[1]-T.B[0])),1.55);

/* ==========================================================================
   A - 0.0-3.0  "IT STARTED WITH ONE."
   ========================================================================== */
function segA(t){
  const u=seg(t,T.A[0],T.A[1]);
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  const gl=eOut(cl(u/0.55));
  let g=x.createRadialGradient(W/2,H*0.47,0,W/2,H*0.47,760);
  g.addColorStop(0,`rgba(201,162,75,${0.20*gl})`); g.addColorStop(1,'rgba(201,162,75,0)');
  x.fillStyle=g; x.fillRect(0,0,W,H);
  const rp=seg(t,0.10,1.25);
  if (rp>0&&rp<1){
    x.save(); x.globalAlpha=(1-rp)*0.5; x.strokeStyle=C.goldHi; x.lineWidth=3;
    x.beginPath(); x.arc(W/2,H*0.47,80+eOut(rp)*470,0,7); x.stroke(); x.restore();
  }
  const ca=cl((u-0.05)/0.20);
  const sc=lp(0.66,1.16,eIOQ(cl(u/0.62)));       // smoother, slower push
  const yo=lp(46,0,eIOQ(cl(u/0.70)));
  x.save(); x.globalAlpha=ca;
  x.translate(W/2,H*0.47+yo); x.scale(sc,sc);
  x.shadowColor='rgba(0,0,0,0.72)'; x.shadowBlur=64; x.shadowOffsetY=18;
  x.drawImage(CARDS[0],-CW/2,-CH/2);
  x.restore();
  const sa=seg(t,1.30,1.95);
  if (sa>0){
    x.save(); x.globalAlpha=cl(sa)*cl((T.A[1]-t)/0.30);
    x.fillStyle='rgba(245,240,232,0.88)'; x.font=`500 40px ${SANS}`; x.textBaseline='middle';
    track(x,'IT STARTED WITH ONE.',W/2,H*0.705,12,'center');
    x.restore();
  }
  vignette(x,0.72); grain(x,t);
}

/* ==========================================================================
   B - 3.0-7.2  one review becomes thousands
   ========================================================================== */
function segB(t){
  const u=seg(t,T.B[0],T.B[1]);
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  drawTunnel(camZat(t), 0.35+0.55*u, 1);
  const words=[['ONE EXPERIENCE.',3.05,4.25],['ONE STORY.',4.32,5.42],['ONE REVIEW.',5.50,7.15]];
  for (const [txt,a,b] of words){
    if (t<a||t>b) continue;
    const p=(t-a)/(b-a);
    const al=cl(p/0.18)*cl((1-p)/0.22);
    x.save(); x.globalAlpha=al;
    x.fillStyle=C.ivory; x.font=`300 ${SZ.bWord}px ${SERIF}`;
    x.textAlign='center'; x.textBaseline='middle';
    x.shadowColor='rgba(0,0,0,0.9)'; x.shadowBlur=48;
    x.fillText(txt,W/2,H*0.5+lp(16,-16,eIO(p)));
    x.restore();
  }
  vignette(x,0.80); grain(x,t);
}

/* ==========================================================================
   C - 7.2-8.6  freeze
   ========================================================================== */
function segC(t){
  const u=seg(t,T.C[0],T.C[1]);
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  drawTunnel(camZat(T.B[1]), 0.9*(1-u*0.5), 1);
  x.save(); x.globalCompositeOperation='saturation';
  x.fillStyle='rgb(128,128,128)'; x.globalAlpha=cl(u/0.25)*0.88; x.fillRect(0,0,W,H);
  x.restore();
  x.fillStyle=`rgba(6,6,8,${cl(u/0.32)*0.66})`; x.fillRect(0,0,W,H);
  const hw=eOutQ(cl((u-0.08)/0.45))*560;
  x.save(); x.globalAlpha=0.9; x.strokeStyle=C.gold; x.lineWidth=2;
  x.beginPath(); x.moveTo(W/2-hw/2,H*0.395); x.lineTo(W/2+hw/2,H*0.395); x.stroke(); x.restore();
  const a=cl((u-0.12)/0.28)*cl((1-u)/0.18);
  x.save(); x.globalAlpha=a;
  x.fillStyle=C.ivory; x.font=`300 ${SZ.cLine}px ${SERIF}`; x.textAlign='center'; x.textBaseline='middle';
  x.fillText('BUT THIS STORY WAS',W/2,H*0.485);
  x.fillText('NEVER BUILT IN ONE PLACE.',W/2,H*0.485+SZ.cLine*1.19);
  x.restore();
  vignette(x,0.85); grain(x,t);
}

/* ==========================================================================
   D - 8.6-26.6  branch run, 9 x 2.0s, centred editorial block
   ========================================================================== */
const CUM=[]; (function(){ let s=0; for (const b of BRANCHES){ s+=b.count; CUM.push(s); } })();
const NB = BRANCHES.length;

function fitFont(txt,maxW,start,weight,fam,tracking){
  let s=start;
  for (; s>40; s-=2){
    x.font=`${weight} ${s}px ${fam}`;
    if (trackW(x,txt,tracking) <= maxW) break;
  }
  return s;
}
function plate(i,u,extraScale=1){
  const im=IMG['b'+String(i+1).padStart(2,'0')];
  const dir=(i%2)?1:-1;
  const sc=lp(1.14,1.02,eIOQ(cl(u)))*extraScale;      // slower, smoother Ken Burns
  cover(x,im,0,0,W,H,sc, dir*lp(0.05,-0.05,eIO(cl(u)))*0.55, lp(0.04,-0.04,eIO(cl(u)))*0.35);
  let g=x.createLinearGradient(0,H*0.30,0,H);
  g.addColorStop(0,'rgba(4,4,6,0)'); g.addColorStop(0.48,'rgba(4,4,6,0.66)'); g.addColorStop(1,'rgba(4,4,6,0.95)');
  x.fillStyle=g; x.fillRect(0,0,W,H);
  g=x.createLinearGradient(0,0,0,H*0.30);
  g.addColorStop(0,'rgba(4,4,6,0.74)'); g.addColorStop(1,'rgba(4,4,6,0)');
  x.fillStyle=g; x.fillRect(0,0,W,H*0.30);
  x.fillStyle='rgba(201,162,75,0.045)'; x.fillRect(0,0,W,H);
}
function clipFor(i,p){
  const e=eIOQ(cl(p));
  switch(i%8){
    case 1: x.beginPath(); x.rect(0,0,W*e,H); x.clip(); break;
    case 2: x.beginPath(); for(let k=0;k<6;k++){ const kp=cl((p-k*0.05)/0.75); x.rect(k*W/6,0,W/6+1,H*eIOQ(kp)); } x.clip(); break;
    case 3: x.beginPath(); x.rect(W/2-W/2*e,0,W*e,H); x.clip(); break;
    case 5: x.beginPath(); x.rect(0,H/2-H/2*e,W,H*e); x.clip(); break;
    case 6: x.beginPath(); x.arc(W/2,H*0.5,e*1180,0,7); x.clip(); break;
    case 7: x.beginPath(); x.rect(0,H-H*e,W,H*e); x.clip(); break;
    default: break;
  }
}
function segD(t){
  const i = cl(Math.floor((t-T.D[0])/SLOT), 0, NB-1);
  const t0 = T.D[0]+i*SLOT, u = (t-t0)/SLOT;
  const p  = cl(u/0.30);                              // slower, smoother transition
  const b  = BRANCHES[i];

  if (i>0) plate(i-1,1.0);
  else { x.fillStyle=C.ink; x.fillRect(0,0,W,H); drawTunnel(camZat(T.B[1]),0.25,0.42);
         x.fillStyle='rgba(6,6,8,0.74)'; x.fillRect(0,0,W,H); }

  x.save(); clipFor(i,p);
  plate(i,u, (i%8)===4 ? lp(1.45,1.0,eOutQ(p)) : 1);
  x.restore();

  // mechanic accents
  if (i===0 && p<1){
    const q=eIn(p), s=lp(0.8,7.5,q);
    x.save(); x.globalAlpha=(1-p)*0.95; x.translate(W/2,H*0.46); x.scale(s,s);
    x.drawImage(CARDS[1],-CW/2,-CH/2); x.restore();
  }
  const e=eIOQ(cl(p));
  if ((i%8)===1&&p<1){ x.save(); x.globalAlpha=(1-p); x.fillStyle=C.goldHi; x.fillRect(W*e-5,0,6,H); x.restore(); }
  if ((i%8)===2&&p<1){ x.save(); x.globalAlpha=(1-p)*0.85; x.fillStyle=C.goldHi;
    for(let k=0;k<6;k++){ const kp=cl((p-k*0.05)/0.75); x.fillRect(k*W/6,H*eIOQ(kp)-4,W/6,5); } x.restore(); }
  if ((i%8)===3&&p<1){ x.save(); x.globalAlpha=(1-p); x.fillStyle=C.goldHi;
    x.fillRect(W/2-W/2*e-4,0,5,H); x.fillRect(W/2+W/2*e,0,5,H); x.restore(); }
  if ((i%8)===6&&p<1){ x.save(); x.globalAlpha=(1-p)*0.9; x.strokeStyle=C.goldHi; x.lineWidth=4;
    x.beginPath(); x.arc(W/2,H*0.5,e*1180,0,7); x.stroke(); x.restore(); }
  if ((i%8)===7&&p<1){ x.save(); x.globalAlpha=(1-p); x.fillStyle=C.goldHi; x.fillRect(0,H-H*e-5,W,6); x.restore(); }
  if (p<0.14) { x.fillStyle=`rgba(245,240,232,${(1-p/0.14)*0.14})`; x.fillRect(0,0,W,H); }

  /* ---- overlays (centred, larger) ---- */
  const oa = cl((u-0.16)/0.18) * cl((1-u)/0.12);
  if (oa<=0){ grain(x,t); return; }
  x.save(); x.globalAlpha=oa; x.textAlign='left'; x.textBaseline='middle';

  // ID (top centre)
  x.fillStyle='rgba(245,240,232,0.66)'; x.font=`500 36px ${SANS}`;
  track(x, `${b.id} / ${String(NB).padStart(2,'0')}`, W/2, 150, 10, 'center');

  // running total (top, centred under the ID)
  const prev = i ? CUM[i-1] : 0;
  const target = (i===NB-1) ? HANDOFF : CUM[i];      // last branch hands off to the counter
  const shown = lp(prev, target, eOutQ(cl((u-0.14)/0.66)));
  x.fillStyle='rgba(245,240,232,0.46)'; x.font=`500 26px ${SANS}`;
  track(x,'RUNNING TOTAL',W/2,214,7,'center');
  x.fillStyle=C.goldHi; x.font=`700 76px ${SANS}`;
  track(x, nfmt(shown), W/2, 274, 2, 'center');

  // centred editorial block
  const by=H*0.660;
  const rw = lp(0,150,eOutQ(cl((u-0.16)/0.34)));
  x.strokeStyle=C.gold; x.lineWidth=3;
  x.beginPath(); x.moveTo(W/2-rw/2,by); x.lineTo(W/2+rw/2,by); x.stroke();

  const fs=fitFont(b.name, W-170, 120, '800', SANS, 3);
  x.fillStyle=C.ivory; x.font=`800 ${fs}px ${SANS}`;
  track(x,b.name,W/2,by+78,3,'center');

  x.fillStyle=C.gold; x.font=`400 40px ${SANS}`;
  track(x,b.city,W/2,by+150,14,'center');

  // stars + rating - measured so they can never overlap
  const SS=32, GAP=40;
  x.font=`600 36px ${SANS}`;
  const rtxt=`${b.rating}   ·   +${nfmt(b.count)} GOOGLE REVIEWS`;
  const tw=trackW(x,rtxt,2.5);
  const sw=starsW(SS);
  const totW=sw+GAP+tw;
  const sx=W/2-totW/2;
  stars(x, sx, by+218, SS, 5);
  x.fillStyle='rgba(245,240,232,0.86)';
  track(x, rtxt, sx+sw+GAP, by+218, 2.5, 'left');

  // real review snippet
  const ra=cl((u-0.40)/0.20)*cl((1-u)/0.16);
  if (ra>0){
    x.save(); x.globalAlpha=oa*ra;
    x.fillStyle='rgba(245,240,232,0.90)'; x.font=`400 italic 46px ${SERIF}`;
    x.textAlign='center';
    const L=wrap(x,'“'+b.reviews[0].t+'”',W-150).slice(0,2);
    L.forEach((s,k)=>x.fillText(s,W/2,H*0.855+k*58));
    x.textAlign='left';
    x.fillStyle='rgba(201,162,75,0.80)'; x.font=`500 27px ${SANS}`;
    track(x, `— ${b.reviews[0].a.toUpperCase()},  ${b.reviews[0].d.toUpperCase()}`,
          W/2, H*0.855+L.length*58+14, 3.5, 'center');
    x.restore();
  }
  x.restore();

  // progress ticks
  x.save(); x.globalAlpha=oa*0.95;
  const tw2=80, gp=12, sx2=(W-(NB*tw2+(NB-1)*gp))/2;
  for (let k=0;k<NB;k++){
    const fill = k===i ? tw2*cl(u/0.96) : tw2;
    x.fillStyle = k<i ? 'rgba(245,240,232,0.44)' : k===i ? C.goldHi : 'rgba(245,240,232,0.14)';
    x.fillRect(sx2+k*(tw2+gp),H-74,fill,3);
    if (k===i){ x.fillStyle='rgba(245,240,232,0.14)'; x.fillRect(sx2+k*(tw2+gp)+fill,H-74,tw2-fill,3); }
  }
  x.restore();
  grain(x,t);
}

/* ==========================================================================
   E - 26.6-31.0  the counter apex : 9,999 -> 10,000 -> 10,271
   ========================================================================== */
const MS = MILESTONE;
let PUNCH = 0.05;
function counterVal(t){
  if (t < 28.40) return lp(HANDOFF, MS-3, eOutQ(seg(t,26.60,28.40)));
  if (t < 28.75) return MS-2;                       // 9,998
  if (t < 29.62) return MS-1;                       // 9,999  (29.10-29.62 = silence)
  if (t < 30.08) return MS;                         // 10,000 - the milestone, held
  if (t < 30.60) return lp(MS, TOTAL, eOutQ(seg(t,30.08,30.60)));
  return TOTAL;
}
function segE(t){
  const u=seg(t,T.E[0],T.E[1]);
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  x.save(); x.globalAlpha=0.30*(1-u*0.5); drawTunnel(camZat(T.B[1])+18+u*8,0,0.5); x.restore();

  const silence = (t>=29.10 && t<29.62);
  const hit     = seg(t,29.62,30.08);
  const racing  = t<28.40;
  const v = counterVal(t);
  const crossed = v>=MS;

  // energetic pulse ring on every tick while racing
  if (racing){
    const beat=(t*7.5)%1;
    x.save(); x.globalAlpha=(1-beat)*0.16; x.strokeStyle=C.goldHi; x.lineWidth=3;
    x.beginPath(); x.arc(W/2,H*0.455,240+beat*420,0,7); x.stroke(); x.restore();
  }
  // label
  x.save(); x.globalAlpha=cl((u-0.02)/0.10)*(silence?0.32:0.78)*cl((T.E[1]-t)/0.35);
  x.fillStyle='rgba(245,240,232,0.80)'; x.font=`500 32px ${SANS}`; x.textBaseline='middle';
  track(x,'ACROSS THE VENUS NETWORK',W/2,H*0.300,10,'center'); x.restore();

  // number
  let sc=1, glow=0;
  if (racing) sc = 1 + Math.sin((t*7.5)%1*Math.PI)*0.022;
  if (silence) sc = 1 + Math.sin((t-29.10)/0.52*Math.PI)*0.014;
  if (hit>0){ sc = 1 + Math.sin(cl(hit/0.40)*Math.PI)*PUNCH; glow = 1-cl(hit/0.95); }
  x.save(); x.translate(W/2,H*0.455); x.scale(sc,sc);
  if (glow>0){
    const g=x.createRadialGradient(0,0,0,0,0,760);
    g.addColorStop(0,`rgba(232,200,116,${0.46*glow})`); g.addColorStop(1,'rgba(232,200,116,0)');
    x.fillStyle=g; x.fillRect(-W,-H/2,W*2,H);
  }
  x.font=`800 ${SZ.counter}px ${SANS}`; x.textAlign='center'; x.textBaseline='middle';
  x.fillStyle = crossed ? C.goldHi : C.ivory;
  x.shadowColor='rgba(0,0,0,0.82)'; x.shadowBlur=56;
  x.fillText(nfmt(v),0,0);
  x.restore();

  if (silence){
    const q=(t-29.10)/0.52;
    x.save(); x.globalAlpha=0.58*Math.sin(q*Math.PI);
    x.strokeStyle=C.gold; x.lineWidth=2;
    x.strokeRect(W/2-520,H*0.455-180,1040,360); x.restore();
  }
  if (hit>0&&hit<1){
    x.save();
    x.globalAlpha=(1-hit)*0.80; x.strokeStyle=C.goldHi; x.lineWidth=7;
    x.beginPath(); x.arc(W/2,H*0.455,150+eOut(hit)*980,0,7); x.stroke();
    x.globalAlpha=(1-hit)*0.50; x.lineWidth=4;
    x.beginPath(); x.arc(W/2,H*0.455,100+eOut(hit)*640,0,7); x.stroke();
    x.globalAlpha=(1-hit)*0.30; x.lineWidth=2;
    x.beginPath(); x.arc(W/2,H*0.455,60+eOut(hit)*380,0,7); x.stroke();
    x.restore();
    x.fillStyle=`rgba(245,240,232,${(1-cl(hit/0.16))*0.44})`; x.fillRect(0,0,W,H);
  }
  // last review lands into the number
  const drop=seg(t,29.34,29.66);
  if (drop>0&&drop<1){
    x.save(); x.globalAlpha=cl(drop/0.28)*(1-cl((drop-0.6)/0.4));
    const s=lp(0.9,0.32,eIn(drop));
    x.translate(W/2,lp(-300,H*0.455,eIn(drop))); x.scale(s,s);
    x.drawImage(CARDS[16 % CARDS.length],-CW/2,-CH/2); x.restore();
  }
  // sublabel
  x.save(); x.globalAlpha=cl((u-0.05)/0.12)*(silence?0.36:0.88)*cl((T.E[1]-t)/0.35);
  x.fillStyle='rgba(245,240,232,0.74)'; x.font=`500 34px ${SANS}`; x.textBaseline='middle';
  track(x,'GOOGLE REVIEWS',W/2,H*0.585,12,'center'); x.restore();
  // still counting
  const sc2=seg(t,30.62,30.90);
  if (sc2>0){
    x.save(); x.globalAlpha=cl(sc2)*cl((T.E[1]-t)/0.22);
    x.fillStyle=C.goldHi; x.font=`400 italic ${SZ.still}px ${SERIF}`;
    x.textAlign='center'; x.textBaseline='middle';
    x.fillText('AND WE’RE STILL COUNTING.',W/2,H*0.672); x.restore();
  }
  vignette(x,0.80); grain(x,t);
}

/* ==========================================================================
   F - 31.0-36.6  hero VFX : 10,000+ built from review cards -> Venus logo
   ========================================================================== */
function segF(t){
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  const p1=seg(t,31.0,32.7), p2=seg(t,32.7,33.9), p3=seg(t,33.9,35.6), p4=seg(t,35.6,36.5);
  const pull=lp(1.0,0.72,eIOQ(p1));
  const cy=H*0.455;
  const NS=(SZ.fMark/NUM_FONT)*pull;
  const LS=780/LOGO_W;

  const solidA=1-cl(seg(t,31.15,32.05));
  if (solidA>0){
    x.save(); x.globalAlpha=solidA; x.translate(W/2,cy); x.scale(pull,pull);
    x.font=`800 ${SZ.fMark}px ${SANS}`; x.textAlign='center'; x.textBaseline='middle';
    x.fillStyle=C.goldHi; x.fillText(MARK,0,0); x.restore();
  }
  const pa=cl(seg(t,31.25,32.15))*(1-cl(p4/0.70));
  if (pa>0){
    x.save(); x.globalAlpha=pa;
    for (let i=0;i<PARTS.length;i++){
      const q=PARTS[i];
      let px=W/2+q.ax*NS, py=cy+q.ay*NS;
      if (p2>0){
        const e2=eOut(cl((p2-q.dl*0.16)/(1-q.dl*0.16)));
        const sw=q.sd*6.283+p2*2.4;
        px+=q.ex*e2+Math.cos(sw)*44*e2; py+=q.ey*e2+Math.sin(sw)*44*e2;
      }
      if (p3>0){
        const e3=eOutQ(cl((p3-q.dl*0.13)/(1-q.dl*0.13)));
        px=lp(px,W/2+q.bx*LS,e3); py=lp(py,H*0.462+q.by*LS,e3);
      }
      const heat=cl(p2)*(1-cl(p3*1.15));
      const w0=q.sz*2.05, h0=q.sz*1.35;
      x.fillStyle = heat>0.35 ? 'rgba(232,200,116,0.95)' : 'rgba(245,240,232,0.94)';
      x.fillRect(px-w0/2,py-h0/2,w0,h0);
      if (q.sz>4.4){ x.fillStyle='rgba(201,162,75,0.85)'; x.fillRect(px-w0/2,py-h0/2,w0,1.4); }
    }
    x.restore();
    const bl=cl(seg(t,31.4,32.1))*(1-cl(p4/0.6));
    if (bl>0){
      const g=x.createRadialGradient(W/2,cy,0,W/2,cy,700);
      g.addColorStop(0,`rgba(201,162,75,${0.17*bl})`); g.addColorStop(1,'rgba(201,162,75,0)');
      x.fillStyle=g; x.fillRect(0,0,W,H);
    }
  }
  if (p4>0){
    x.save(); x.globalAlpha=eOut(p4);
    const lw=780, lh=lw*IMG.logo.height/IMG.logo.width;
    x.drawImage(IMG.logo,W/2-lw/2,H*0.462-lh/2,lw,lh); x.restore();
  }
  const sa=seg(t,31.6,32.05)*(1-cl(seg(t,33.2,33.6)));
  if (sa>0){
    x.save(); x.globalAlpha=cl(sa);
    x.fillStyle='rgba(245,240,232,0.88)'; x.font=`500 36px ${SANS}`; x.textBaseline='middle';
    track(x,'GOOGLE REVIEWS',W/2,H*0.625,12,'center'); x.restore();
  }
  const ea=seg(t,35.9,36.35);
  if (ea>0){
    x.save(); x.globalAlpha=cl(ea)*0.92;
    x.fillStyle=C.gold; x.font=`500 30px ${SANS}`; x.textBaseline='middle';
    track(x,'ONE STANDARD. EVERY CITY.',W/2,H*0.585,9,'center'); x.restore();
  }
  vignette(x,0.78); grain(x,t);
}

/* ==========================================================================
   G - 36.6-42.2  treatment montage (real Venus clinical photography)
   ========================================================================== */
const MSHOT=0.70;
function segG(t){
  const k=cl(Math.floor((t-T.G[0])/MSHOT),0,7);
  const u=(t-(T.G[0]+k*MSHOT))/MSHOT;
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  const push=(k%2===0);
  const sc=push?lp(1.17,1.03,eIOQ(u)):lp(1.03,1.17,eIOQ(u));
  const dir=(k%3)-1;
  cover(x,IMG['t'+k],0,0,W,H,sc,dir*lp(0.06,-0.06,eIO(u))*0.6,lp(0.04,-0.04,eIO(u))*0.4);
  let g=x.createLinearGradient(0,0,0,H);
  g.addColorStop(0,'rgba(6,5,4,0.58)'); g.addColorStop(0.42,'rgba(6,5,4,0.16)'); g.addColorStop(1,'rgba(6,5,4,0.88)');
  x.fillStyle=g; x.fillRect(0,0,W,H);
  x.fillStyle='rgba(201,162,75,0.07)'; x.fillRect(0,0,W,H);
  if (u<0.06){ x.fillStyle=`rgba(245,240,232,${(1-u/0.06)*0.12})`; x.fillRect(0,0,W,H); }
  if (u<0.04){ x.fillStyle=`rgba(4,4,6,${(1-u/0.04)*0.50})`; x.fillRect(0,0,W,H); }
  const ca=seg(t,37.1,37.75)*(1-cl(seg(t,41.35,41.95)));
  if (ca>0){
    x.save(); x.globalAlpha=cl(ca);
    x.fillStyle=C.ivory; x.font=`300 ${SZ.gLine}px ${SERIF}`; x.textAlign='center'; x.textBaseline='middle';
    x.shadowColor='rgba(0,0,0,0.92)'; x.shadowBlur=48;
    x.fillText('BEHIND EVERY REVIEW',W/2,H*0.735);
    x.fillText('IS A STORY OF TRUST.',W/2,H*0.735+SZ.gLine*1.17);
    x.restore();
  }
  x.save(); x.globalAlpha=0.5; x.fillStyle=C.gold;
  x.fillRect(76,H-74,(W-152)*cl((t-T.G[0])/(T.G[1]-T.G[0])),2); x.restore();
  vignette(x,0.72); grain(x,t);
}

/* ==========================================================================
   H - 42.2-45.0  end frame
   ========================================================================== */
function segH(t){
  const u=seg(t,T.H[0],T.H[1]);
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  const g=x.createRadialGradient(W/2,H*0.40,0,W/2,H*0.40,1000);
  g.addColorStop(0,`rgba(201,162,75,${0.14*cl(u/0.3)})`); g.addColorStop(1,'rgba(201,162,75,0)');
  x.fillStyle=g; x.fillRect(0,0,W,H);

  const la=cl(seg(t,42.20,42.75));
  x.save(); x.globalAlpha=la;
  const lw=720, lh=lw*IMG.logo.height/IMG.logo.width;
  x.drawImage(IMG.logo,W/2-lw/2,H*0.290-lh/2+lp(28,0,eOutQ(la)),lw,lh); x.restore();

  const ra=cl(seg(t,42.60,43.05));
  x.save(); x.globalAlpha=ra; x.strokeStyle=C.gold; x.lineWidth=2;
  x.beginPath(); x.moveTo(W/2-180*ra,H*0.398); x.lineTo(W/2+180*ra,H*0.398); x.stroke(); x.restore();

  x.textBaseline='middle';
  const na=cl(seg(t,42.72,43.24));
  x.save(); x.globalAlpha=na; x.textAlign='center';
  x.fillStyle=C.ivory; x.font=`800 ${SZ.hMark}px ${SANS}`;
  x.fillText(MARK,W/2,H*0.487+lp(16,0,eOutQ(na)));
  x.restore();

  const ca=cl(seg(t,42.95,43.45));
  x.save(); x.globalAlpha=ca;
  x.fillStyle='rgba(245,240,232,0.90)'; x.font=`500 ${SZ.hStmt}px ${SANS}`;
  track(x,'TIMES YOU CHOSE VENUS.',W/2,H*0.573,7,'center'); x.restore();

  const ga=cl(seg(t,43.25,43.78));
  x.save(); x.globalAlpha=ga;
  x.fillStyle=C.goldHi; x.font=`400 italic ${SZ.thanks}px ${SERIF}`; x.textAlign='center';
  x.fillText('THANK YOU, PAKISTAN.',W/2,H*0.667); x.restore();

  const pa=cl(seg(t,43.62,44.10));
  x.save(); x.globalAlpha=pa*0.94;
  stars(x, W/2-starsW(30)/2, H*0.752, 30, 5);
  x.fillStyle='rgba(245,240,232,0.66)'; x.font=`500 30px ${SANS}`;
  track(x,`${nfmt(TOTAL)} GOOGLE REVIEWS`,W/2,H*0.798,8,'center');
  x.fillStyle='rgba(245,240,232,0.34)'; x.font=`400 23px ${SANS}`;
  track(x,`VERIFIED ON GOOGLE · ${CAPTURE_DATE}`,W/2,H*0.838,4,'center');
  x.restore();

  const fo=seg(t,44.58,45.0);
  if (fo>0){ x.fillStyle=`rgba(8,8,10,${fo})`; x.fillRect(0,0,W,H); }
  grain(x,t,0.016);
}

/* ==========================================================================
   DISPATCH
   ========================================================================== */
function seek(t){
  t=cl(t,0,DUR-0.0001);
  x.textAlign='left'; x.textBaseline='alphabetic';
  x.fillStyle=C.ink; x.fillRect(0,0,W,H);
  if      (t<T.A[1]) segA(t);
  else if (t<T.B[1]) segB(t);
  else if (t<T.C[1]) segC(t);
  else if (t<T.D[1]) segD(t);
  else if (t<T.E[1]) segE(t);
  else if (t<T.F[1]) segF(t);
  else if (t<T.G[1]) segG(t);
  else               segH(t);
}
window.seek = seek;

(async function boot(){
  await loadFonts();
  await loadAssets();
  buildCards(); buildTunnel(); buildParticles(); buildSizes();
  seek(0);
  window.READY = true;
})();
