#!/usr/bin/node

const d = process.argv.slice(2);
if (d.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i < d.length; i++) {
    d[i] = parseInt(d[i]);
  }
  const big = Math.max(...d);
  d[d.indexOf(big)] = -Infinity;
  console.log(Math.max(...d));
}
