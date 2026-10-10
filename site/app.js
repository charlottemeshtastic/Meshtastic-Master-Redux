/* Browser-only directory: no network requests, accounts or third-party tracking. */
'use strict';
const records = JSON.parse(document.getElementById('resource-data').textContent).sort((a,b) => a.name.localeCompare(b.name));
const PAGE_SIZE = 24;
const controls = Object.fromEntries(['search','category','platform','country'].map(id => [id,document.getElementById(id)]));
const params = new URLSearchParams(location.hash.slice(1));
let view = ['resources','communities','all'].includes(params.get('view')) ? params.get('view') : 'resources';
let page = Math.max(1, Number.parseInt(params.get('page'),10) || 1);
function option(select, value) { const e=document.createElement('option'); e.value=value; e.textContent=value; select.append(e); }
[...new Set(records.map(r=>r.category))].sort().forEach(v=>option(controls.category,v));
[...new Set(records.flatMap(r=>r.platforms))].sort().forEach(v=>option(controls.platform,v));
[...new Set(records.map(r=>r.country).filter(Boolean))].sort().forEach(v=>option(controls.country,v));
for (const [id,control] of Object.entries(controls)) { const value=params.get(id)||''; if(control.tagName==='INPUT'||[...control.options].some(o=>o.value===value)) control.value=value; }
function text(tag, value, className) { const e=document.createElement(tag);e.textContent=value;if(className)e.className=className;return e; }
function link(value, url) { const e=text('a',value);e.href=url;e.rel='noreferrer noopener';return e; }
function safeUrl(url) { try { const u=new URL(url);return ['https:','http:'].includes(u.protocol) ? u.href : null; } catch { return null; } }
function render() {
  const state=Object.fromEntries(Object.entries(controls).map(([id,e])=>[id,e.value]));state.view=view;
  const matches=MeshDirectory.matching(records,state),pages=Math.max(1,Math.ceil(matches.length/PAGE_SIZE));page=Math.min(page,pages);
  const results=document.getElementById('results');results.replaceChildren();
  for (const r of matches.slice((page-1)*PAGE_SIZE,page*PAGE_SIZE)) {
    const card=text('article','', 'resource');const top=text('div','', 'resource-top');top.append(text('span',r.category,'category-badge'),text('span','↗','outbound'));card.append(top);
    const h=text('h3',''),url=safeUrl(r.url);h.append(url?link(r.name,url):text('span',r.name));card.append(h,text('p',r.description||[r.country,r.region].filter(Boolean).join(' · ')||'Explore this community resource.','resource-description'));
    if(r.links.length) {const extra=text('div','','extra-links');for(const l of r.links){const u=safeUrl(l.url);if(u)extra.append(link(l.name,u));}card.append(extra);}
    const meta=text('div','','resource-meta');for(const tag of [...r.platforms,r.country,r.region].filter(Boolean))meta.append(text('span',tag,'tag'));card.append(meta);
    const status={'pending':'Verification pending','membership-unverified':'Membership not verified','listed':'Listed in the index'}[r.status]||'Listed in the index';card.append(text('span',status,'status'+(r.status==='pending'?' pending':'')));
    const source=link('View source entry',`https://github.com/charlottemeshtastic/Meshtastic-Master-Redux/blob/${document.body.dataset.sourceRef||'main'}/${r.source}#L${r.line}`);source.className='resource-source';card.append(source);results.append(card);
  }
  const start=matches.length?(page-1)*PAGE_SIZE+1:0,end=Math.min(page*PAGE_SIZE,matches.length);
  document.getElementById('result-count').textContent=`${matches.length} ${matches.length===1?'match':'matches'} · Showing ${start}–${end}`;
  document.getElementById('empty').hidden=matches.length>0;document.getElementById('page-label').textContent=`Page ${page} of ${pages}`;
  document.getElementById('previous').disabled=page<=1;document.getElementById('next').disabled=page>=pages;
  document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===view)));
  const p=new URLSearchParams();for(const [k,v] of Object.entries(state))if(v)p.set(k,v);if(page>1)p.set('page',String(page));history.replaceState(null,'','#'+p.toString());
}
function reset() {for(const e of Object.values(controls))e.value='';view='resources';page=1;render();}
document.getElementById('filters').addEventListener('submit',e=>e.preventDefault());
controls.search.addEventListener('input',()=>{page=1;render();});
for(const name of ['category','platform','country'])controls[name].addEventListener('change',()=>{if(name==='country'&&controls.country.value)view='communities';if(name==='category'&&controls.category.value)view=controls.category.value==='Communities'?'communities':'resources';page=1;render();});
document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>{view=b.dataset.view;controls.category.value='';controls.country.value='';page=1;render();}));
for(const id of ['clear','empty-reset'])document.getElementById(id).addEventListener('click',reset);
for(const [id,delta] of [['previous',-1],['next',1]])document.getElementById(id).addEventListener('click',()=>{page+=delta;render();document.getElementById('directory-title').scrollIntoView({block:'start'});} );
document.getElementById('share').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(location.href);document.getElementById('result-count').textContent='View link copied.';}catch{document.getElementById('result-count').textContent='Copy the address in your browser to share this view.';}});
render();
