(()=>{
const tabs=[...document.querySelectorAll('.tab')],pages=[...document.querySelectorAll('.page')];let active='overview';const levels={};
function view(){return document.querySelector('#view-'+active)}
function fitZoom(){const el=view(),v=el.querySelector('.viewport'),s=el.querySelector('svg.diagram');const w=Number(s.dataset.baseW);return Math.min(1.10,Math.max(.05,(v.clientWidth-56)/w))}
function zoom(n,center=true){const el=view(); if(!el)return;const s=el.querySelector('svg.diagram'),v=el.querySelector('.viewport'),w=Number(s.dataset.baseW),h=Number(s.dataset.baseH);const old=levels[active]||fitZoom();n=Math.max(.05,Math.min(2.8,n));if(center){const cx=(v.scrollLeft+v.clientWidth/2)/(w*old),cy=(v.scrollTop+v.clientHeight/2)/(h*old);s.setAttribute('width',String(w*n));s.setAttribute('height',String(h*n));levels[active]=n;v.scrollLeft=cx*w*n-v.clientWidth/2;v.scrollTop=cy*h*n-v.clientHeight/2;}else{s.setAttribute('width',String(w*n));s.setAttribute('height',String(h*n));levels[active]=n;v.scrollLeft=0;v.scrollTop=0;}document.querySelector('#zoomvalue').textContent=Math.round(n*100)+'%';}
function activate(id,doHash=true){if(!document.querySelector('#view-'+id))id='overview';active=id;tabs.forEach(t=>{const on=t.dataset.tab===id;t.classList.toggle('active',on);t.setAttribute('aria-selected',String(on));});pages.forEach(p=>p.classList.toggle('active',p.dataset.key===id));if(doHash)history.replaceState(null,'','#'+id);requestAnimationFrame(()=>zoom(levels[id]||fitZoom(),false));}
tabs.forEach(t=>t.addEventListener('click',()=>activate(t.dataset.tab)));
document.querySelector('#zoomin').onclick=()=>zoom((levels[active]||fitZoom())*1.25);
document.querySelector('#zoomout').onclick=()=>zoom((levels[active]||fitZoom())/1.25);
document.querySelector('#fit').onclick=()=>zoom(fitZoom(),false);
document.querySelector('#actual').onclick=()=>zoom(1,false);
window.addEventListener('hashchange',()=>activate(location.hash.replace('#',''),false));
for(const v of document.querySelectorAll('.viewport')){let drag=null;v.addEventListener('pointerdown',e=>{if(e.button!==0||e.target.closest('a'))return;drag={x:e.clientX,y:e.clientY,left:v.scrollLeft,top:v.scrollTop};v.setPointerCapture(e.pointerId);v.classList.add('dragging');});v.addEventListener('pointermove',e=>{if(!drag)return;v.scrollLeft=drag.left+drag.x-e.clientX;v.scrollTop=drag.top+drag.y-e.clientY;});function end(){drag=null;v.classList.remove('dragging');}v.addEventListener('pointerup',end);v.addEventListener('pointercancel',end);v.addEventListener('wheel',e=>{if(e.ctrlKey||e.metaKey){e.preventDefault();zoom((levels[active]||fitZoom())*(e.deltaY<0?1.10:.90));}},{passive:false});}
activate(location.hash.replace('#','')||'overview',false);
})();
