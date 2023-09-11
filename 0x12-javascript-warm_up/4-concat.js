#!/usr/bin/node
// script that prints two arguments passed to it seperated by is

const process = require('process');
const argv = process.argv;

console.log(`${argv[2]} is ${argv[3]}`);
