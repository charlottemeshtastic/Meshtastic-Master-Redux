'use strict';
const assert = require('node:assert/strict');
const {matching} = require('../site/filters.js');
const rows = [
  {name:'MeshtasticD',description:'Native computer node',category:'Linux and Raspberry Pi',country:'',region:'',platforms:['Linux','macOS']},
  {name:'Charlotte Mesh',description:'Local radio community',category:'Communities',country:'United States',region:'North Carolina',platforms:[]},
  {name:'Ontario Mesh',description:'Local radio community',category:'Communities',country:'Canada',region:'Ontario',platforms:[]}
];
const base = {search:'',category:'',platform:'',country:'',view:'all'};
const filter = (fields) => matching(rows,{...base,...fields});
assert.equal(filter({view:'resources'}).length,1);
assert.equal(filter({view:'communities'}).length,2);
assert.equal(filter({search:'CHARLOTTE radio',country:'United States',category:'Communities',view:'communities'})[0].name,'Charlotte Mesh');
assert.equal(filter({platform:'Linux'})[0].name,'MeshtasticD');
assert.equal(filter({country:'Canada'})[0].name,'Ontario Mesh');
assert.equal(filter({platform:'Linux',country:'Canada'}).length,0);
assert.equal(filter({search:'no such thing'}).length,0);
assert.equal(filter({search:'  native   COMPUTER  '}).length,1);
assert.equal(filter({platform:'Android'}).length,0);
console.log('PASS: combined filters, collections, case-insensitive token search, unknown platforms and empty results.');
