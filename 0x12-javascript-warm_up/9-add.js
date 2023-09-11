#!/usr/bin/node
const myVar = process.argv.slice(2);
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(myVar[0], myVar[1]));