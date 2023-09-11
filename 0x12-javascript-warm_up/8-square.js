#!/usr/bin/node
const myVar = process.argv.slice(2);
const size = parseInt(myVar[0]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let str;
  for (let i = 0; i < size; i++) {
    str = '';
    for (let j = 0; j < size; j++) {
      str += 'X';
    }
    console.log(str);
  }
}