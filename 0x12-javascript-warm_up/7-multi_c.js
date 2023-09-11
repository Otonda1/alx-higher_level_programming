#!/usr/bin/node
const myVar = process.argv.slice(2);
const count = parseInt(myVar[0]);
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
