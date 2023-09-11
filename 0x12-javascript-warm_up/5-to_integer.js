#!/usr/bin/node
// script that prints first argument if it can be convertd to an integer

const process = require('process');

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(process.argv[2])}`);
}
