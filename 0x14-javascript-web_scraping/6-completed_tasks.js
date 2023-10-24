#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const x of tasks) {
      if (x.completed === true) {
        if (x.userId in completed) {
          completed[x.userId]++;
        } else {
          completed[x.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
