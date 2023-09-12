#!/usr/bin/node
exports.esrever = function (list) {
  const newArr = [];
  for (let i = 0; i < list.length; i++) {
    newArr.unshift(list[i]);
  }
  return newArr;
};
