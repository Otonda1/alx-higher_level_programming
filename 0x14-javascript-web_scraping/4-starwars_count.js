#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const cast = (results[i].characters);
      for (let j = 0; j < cast.length; j++) {
        if (cast[j].endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
