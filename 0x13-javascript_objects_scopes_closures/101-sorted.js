#!/usr/bin/node
let hary = require('./101-data.js').dict
let newDict = {};
for (let key in hary) {
  if (newDict[hary[key]] === undefined) {

  
