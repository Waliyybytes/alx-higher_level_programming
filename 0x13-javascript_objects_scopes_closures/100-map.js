#!/usr/bin/node
const first = require('./100-data').list;
const dList = first.map((a, n) => a * n);
console.log(dList);
console.log(first);
