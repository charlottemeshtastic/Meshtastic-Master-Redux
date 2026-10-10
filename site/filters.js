/* Shared, dependency-free filter behavior for the browser and regression tests. */
(function(root) {
'use strict';
function matching(records, state) {
  const tokens=state.search.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
  return records.filter(r => (state.view==='all'||(r.category==='Communities')===(state.view==='communities'))
    && (!state.category||r.category===state.category) && (!state.country||r.country===state.country)
    && (!state.platform||r.platforms.includes(state.platform))
    && tokens.every(t=>`${r.name} ${r.description} ${r.category} ${r.country} ${r.region} ${r.platforms.join(' ')}`.toLocaleLowerCase().includes(t)));
}
const api = {matching};
if (typeof module !== 'undefined' && module.exports) module.exports = api;
else root.MeshDirectory = api;
})(globalThis);
