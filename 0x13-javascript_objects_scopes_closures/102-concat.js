#!/usr/bin/node
const fs = require('fs');
let buffer = fs.readFileSync(process.argv[2], 'utf8');
buffer += fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], buffer);
