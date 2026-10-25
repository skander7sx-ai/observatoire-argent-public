(function(){
 function norm(t){return (t||'').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');}
 var q=document.getElementById('q'); if(!q) return; // pages sans liste de fiches : le formulaire de l'en-tête renvoie vers index.html?q=
 var cards=[].slice.call(document.querySelectorAll('#cards .card'));
 var tbtns=[].slice.call(document.querySelectorAll('.tags-f button'));
 var cbtns=[].slice.call(document.querySelectorAll('.camps-f button'));
 var count=document.getElementById('count'), none=document.getElementById('noresult'), clr=document.getElementById('qclear'), hq=document.getElementById('hq');
 var tag='', camp='';
 function mark(btns,attr,val){btns.forEach(function(b){b.classList.toggle('on',b.getAttribute(attr)===val);});}
 function apply(skipUrl){
  var terms=norm(q.value).split(/\s+/).filter(Boolean), n=0;
  cards.forEach(function(c){
   var hay=c.getAttribute('data-s'), okq=terms.every(function(t){return hay.indexOf(t)>-1;});
   var okt=!tag||c.getAttribute('data-tags').split('|').indexOf(tag)>-1;
   var okc=!camp||c.getAttribute('data-camps').split('|').indexOf(camp)>-1;
   var show=okq&&okt&&okc; c.hidden=!show; if(show)n++;
  });
  var f=[]; if(terms.length)f.push('texte'); if(tag)f.push('thème'); if(camp)f.push('camp');
  count.textContent=n+' fiche'+(n>1?'s':'')+' sur '+cards.length+(f.length?' (filtre : '+f.join(' + ')+')':'');
  none.hidden=n>0; clr.hidden=!(q.value||tag||camp);
  if(hq) hq.value=q.value;
  if(!skipUrl){try{var u=new URL(location.href); [['q',q.value.trim()],['tag',tag],['camp',camp]].forEach(function(p){if(p[1])u.searchParams.set(p[0],p[1]);else u.searchParams.delete(p[0]);}); history.replaceState(null,'',u);}catch(e){}}
 }
 tbtns.forEach(function(b){b.addEventListener('click',function(){tag=b.getAttribute('data-t');mark(tbtns,'data-t',tag);apply();});});
 cbtns.forEach(function(b){b.addEventListener('click',function(){camp=b.getAttribute('data-c');mark(cbtns,'data-c',camp);apply();});});
 q.addEventListener('input',function(){apply();});
 if(hq) hq.addEventListener('input',function(){q.value=hq.value;apply();});
 var hf=document.querySelector('form.hsearch'); if(hf) hf.addEventListener('submit',function(e){e.preventDefault();q.focus();apply();});
 clr.addEventListener('click',function(){q.value='';tag='';camp='';mark(tbtns,'data-t','');mark(cbtns,'data-c','');apply();q.focus();});
 var p=new URLSearchParams(location.search);
 if(p.get('q')) q.value=p.get('q'); tag=p.get('tag')||''; camp=p.get('camp')||'';
 mark(tbtns,'data-t',tag); mark(cbtns,'data-c',camp);
 apply(true);
})();
