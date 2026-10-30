(async function(){
 await document.fonts.ready;fitLines();
 const source=document.getElementById('flow-source'),papers=document.querySelector('.papers');let content;
 function addPage(){const p=document.createElement('section');p.className='paper';p.innerHTML='<div class="flow-content"></div><div class="footer"></div>';papers.append(p);content=p.firstElementChild;}
 function overflows(){return content.scrollHeight>content.clientHeight+1;}
 function moveHeading(){const h=content.lastElementChild?.classList.contains('section-heading')?content.lastElementChild:null;if(h)h.remove();addPage();if(h)content.append(h);}
 function continuation(original){const a=document.createElement('article');a.className='question';a.dataset.number=original.dataset.number;a.dataset.continued='true';a.innerHTML='<div class="qbody"></div>';content.append(a);return a;}
 function splitQuestion(el){
  const body=el.querySelector('.qbody');const parts=[...body.children];const opts=el.querySelector('.options');if(opts)parts.push(opts);
  parts.forEach(p=>p.remove());let article=el;
  for(let i=0;i<parts.length;i++){
   const part=parts[i];let target=part===opts?article:article.querySelector('.qbody');target.append(part);
   let overflow=overflows();
   // A first paragraph stays with its immediately following code or illustration.
   if(i===0&&parts[1]&&['PRE','FIGURE'].includes(parts[1].tagName)){
    target.append(parts[1]);overflow=overflow||overflows();parts[1].remove();
   }
   if(!overflow)continue;
   part.remove();
   if(i===0){el.remove();moveHeading();content.append(el);article=el;}
   else {addPage();article=continuation(el);}
   target=part===opts?article:article.querySelector('.qbody');target.append(part);
   if(overflows())throw Error('Content block exceeds printable page: '+el.dataset.number);
  }
 }
 addPage();
 for(const el of [...source.children]){
  content.append(el);
  const n=Number(el.dataset.number||0);
  if(n>=41){if(overflows())splitQuestion(el);continue;}
  if(!overflows())continue;
  el.remove();moveHeading();content.append(el);
  if(overflows())splitQuestion(el);
 }
 source.remove();
 const pages=[...papers.querySelectorAll('.paper')];pages.forEach((p,i)=>{const f=p.querySelector('.footer');if(f)f.textContent=`第 ${i+1} 页（共 ${pages.length} 页）`;p.setAttribute('aria-label',`第 ${i+1} 页`);});
 window.paperReady=true;document.getElementById('print').disabled=false;document.getElementById('print').onclick=()=>window.print();
})().catch(e=>{window.paperError=String(e);console.error(e)});
