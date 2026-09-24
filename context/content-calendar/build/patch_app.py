# -*- coding: utf-8 -*-
import io

P = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\public\app.js"
s = io.open(P, encoding="utf-8").read()

NEW_DRAWER = r"""function openDrawer(item){
  var d=$('#drawerInner'); d.innerHTML='';
  var e=entryOf(item.id);

  var head=el('div','dhead');
  var hh=el('div');
  hh.appendChild(el('h2',null,item.show));
  hh.appendChild(el('p',null, item.dayFull+' '+item.dateLabel+'   Week '+item.week+'   '+item.block));
  head.appendChild(hh);
  var x=el('button','dclose','\u00d7'); x.setAttribute('aria-label','Close');
  x.addEventListener('click', closeDrawer); head.appendChild(x);
  d.appendChild(head);

  var meta=el('div','dmeta');
  meta.appendChild(el('span','pill hot', item.sourceLabel));
  [item.creative, item.treatment==='None'?'No treatment':item.treatment, item.owner].forEach(function(t){
    meta.appendChild(el('span','pill',t)); });
  d.appendChild(meta);

  var ctr=el('div','controls');
  var sw=el('div'); sw.appendChild(el('label',null,'Status'));
  var sel=el('select');
  STATUSES.forEach(function(k){ var o=el('option',null,SLABEL[k]); o.value=k; sel.appendChild(o); });
  sel.value=e.status;
  sel.addEventListener('change', function(){ save(item.id,{status:sel.value}); });
  sw.appendChild(sel);
  var aw=el('div'); aw.appendChild(el('label',null,'Assigned to'));
  var ai=el('input'); ai.value=e.assignee||''; ai.placeholder='Name';
  ai.addEventListener('change', function(){ save(item.id,{assignee:ai.value}); });
  aw.appendChild(ai);
  ctr.appendChild(sw); ctr.appendChild(aw); d.appendChild(ctr);

  d.appendChild(field('Hook, first line on screen', item.hook, 'hook'));
  d.appendChild(field('Caption', item.caption));
  if(item.hashtags) d.appendChild(field('Hashtags', item.hashtags));
  d.appendChild(field('Call to action', item.cta));

  var af=el('div','field');
  af.appendChild(el('label',null, item.fromDrive?'Footage in your Drive':'What has to be made'));
  var box=el('div','assetbox');
  if(item.fromDrive){
    box.appendChild(el('div','fname', item.driveFile||item.asset));
    box.appendChild(el('div','fpath', item.driveFolder||''));
    if(item.driveUrl){
      var a=el('a','bigbtn','Open in Google Drive');
      a.href=item.driveUrl; a.target='_blank'; a.rel='noopener noreferrer';
      box.appendChild(a);
    }
  } else {
    box.appendChild(el('div','fname', item.asset));
  }
  af.appendChild(box); d.appendChild(af);

  if(item.script){
    var sf=el('div','field');
    var srow=el('div','copyrow');
    srow.appendChild(el('label',null,'The script, word for word'));
    var w=el('div');
    var dl=el('a','btn sm','Download'); dl.href='/api/script/'+item.id+'.txt'; dl.setAttribute('download','');
    var cp=el('button','btn sm','Copy'); cp.style.marginLeft='6px';
    cp.addEventListener('click', function(){
      if(navigator.clipboard) navigator.clipboard.writeText(item.script).then(function(){toast('Copied');});
    });
    w.appendChild(dl); w.appendChild(cp);
    srow.appendChild(w); sf.appendChild(srow);
    sf.appendChild(el('div','val script', item.script));
    d.appendChild(sf);
  }

  if(item.recordGuide) d.appendChild(field('How to record this', item.recordGuide));

  d.appendChild(field(item.creative==='Reel' ? 'Shot by shot spec' : 'Slide by slide spec', item.spec));

  if(item.ref){
    var rf=el('div','field');
    rf.appendChild(el('label',null,'Reference, same format'));
    var rb=el('div','refbox');
    rb.appendChild(el('div','racct', (item.refAccount||'')+'   '+(item.refFormat||'')));
    rb.appendChild(el('div','rwhy', item.refWhy||''));
    rb.appendChild(el('div','rmetric', item.refMetric||''));
    var ra=el('a','bigbtn','Open the reference post');
    ra.href=item.ref; ra.target='_blank'; ra.rel='noopener noreferrer';
    rb.appendChild(ra); rf.appendChild(rb); d.appendChild(rf);
  }

  var cm=el('div','comments');
  cm.appendChild(el('label',null,'Comments ('+((e.comments||[]).length)+')'));
  (e.comments||[]).forEach(function(c){
    var b=el('div','cmt'); var cw=el('div','cw');
    cw.appendChild(el('b',null, c.author+(c.role==='admin'?' (marketing head)':'')));
    cw.appendChild(el('span',null, new Date(c.at).toLocaleString('en-GB')));
    b.appendChild(cw); b.appendChild(el('p',null,c.text)); cm.appendChild(b);
  });
  var form=el('div','cmtform');
  var ta=el('textarea'); ta.placeholder='Note for the team';
  var btn=el('button','btn primary','Post');
  btn.addEventListener('click', function(){
    if(!ta.value.trim()) return;
    save(item.id,{comment:ta.value}).then(function(){ openDrawer(item); });
  });
  form.appendChild(ta); form.appendChild(btn); cm.appendChild(form);
  d.appendChild(cm);

  $('#drawer').hidden=false; $('#scrim').hidden=false; $('#drawer').scrollTop=0;
}

"""

NEW_PLAYBOOK = r"""function renderPlaybook(root){
  var nav=el('div','pbnav');
  [['formats','Formats'],['refs','References']].forEach(function(t){
    var b=el('button',PBTAB===t[0]?'on':null,t[1]);
    b.addEventListener('click', function(){ PBTAB=t[0]; render(); });
    nav.appendChild(b);
  });
  root.appendChild(nav);
  if(PBTAB==='refs') pbRefs(root); else pbFormats(root);
}

function pbFormats(root){
  var p=el('p'); p.style.cssText='margin:0 0 16px;color:var(--ink-soft);font-size:.88rem;max-width:76ch';
  p.textContent='Every recurring format in the quarter, and how many posts each one carries.';
  root.appendChild(p);
  var grid=el('div','grid');
  var counts=CAL.stats.byShow;
  Object.keys(counts).sort(function(a,b){ return counts[b]-counts[a]; }).forEach(function(name){
    var posts=CAL.items.filter(function(i){ return i.show===name; });
    var c=el('div','panel acc'); c.style.setProperty('--fc', FC[name]||'var(--ink)');
    c.appendChild(el('div','meta', counts[name]+' posts'));
    c.appendChild(el('h3',null,name));
    var mix={}; posts.forEach(function(i){ mix[i.sourceLabel]=(mix[i.sourceLabel]||0)+1; });
    c.appendChild(el('p',null, Object.keys(mix).map(function(k){ return mix[k]+' '+k.toLowerCase(); }).join(', ')));
    var rl=el('div','reflinks');
    posts.slice(0,6).forEach(function(i){
      var b=el('a','reflink', i.dateLabel.slice(0,6));
      b.href='#'; b.addEventListener('click', function(ev){ ev.preventDefault(); openDrawer(i); });
      rl.appendChild(b);
    });
    c.appendChild(rl);
    grid.appendChild(c);
  });
  root.appendChild(grid);
}

function pbRefs(root){
  var p=el('p'); p.style.cssText='margin:0 0 16px;color:var(--ink-soft);font-size:.88rem;max-width:76ch';
  p.textContent=CAL.referenceLibrary.length+' reference posts, matched by FORMAT. A carousel post only ever '
    +'references a real carousel. Every one was crawled with its real engagement.';
  root.appendChild(p);
  var grid=el('div','grid');
  CAL.referenceLibrary.forEach(function(r){
    var isCar = r.format && r.format.indexOf('Carousel')>=0;
    var c=el('div','panel acc');
    c.style.setProperty('--fc', isCar ? 'var(--f-is)' : 'var(--f-side)');
    c.appendChild(el('div','meta', r.account+'   '+r.format+'   used on '+r.usedOn));
    c.appendChild(el('h3',null, r.key.replace(/_/g,' ')));
    c.appendChild(el('p',null,r.why));
    var m=el('p'); m.style.cssText='font-size:.77rem;color:var(--ink-faint)'; m.textContent=r.metric; c.appendChild(m);
    var rl=el('div','reflinks');
    var a=el('a','reflink','Open the post'); a.href=r.url; a.target='_blank'; a.rel='noopener noreferrer';
    rl.appendChild(a); c.appendChild(rl);
    grid.appendChild(c);
  });
  root.appendChild(grid);
}

"""

start = s.index("function openDrawer(item){")
end = s.index("function field(label,value,extra){")
s = s[:start] + NEW_DRAWER + s[end:]

ps = s.index("function renderPlaybook(root){")
pe = s.index("/* ============================================================ activity */")
s = s[:ps] + NEW_PLAYBOOK + s[pe:]

io.open(P, "w", encoding="utf-8").write(s)
print("drawer and playbook replaced")
