#!/usr/bin/node

function factorial (n) {
  return (n ? n * factorial(n - 1) : 1);
}

console.log(factorial(parseInt(process.argv[2])));
