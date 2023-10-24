#!/usr/bin/node

const fs = require('fs');
const url = process.argv[2];
const request = require('request');
const file = process.argv[3];

request
  .get(url)
  .pipe(fs.createWriteStream(file));
