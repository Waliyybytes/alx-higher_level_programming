#!/usr/bin/node
const hary = require('./101-data.js').dict;
const newDict = {};
for (const key in hary) {
  if (newDict[hary[key]] === undefined) {
    newDict[hary[key]] = Array(key);
  } else {
    newDict[hary[key]].push(key);
  }
}
console.log(newDict);
