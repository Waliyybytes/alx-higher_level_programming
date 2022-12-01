#!/usr/bin/node
const list = require('./100-data.js').list;
const dList = list.map((a, n) => a * n);
console.log(dList);
console.log(list);
