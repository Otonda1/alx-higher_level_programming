#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let str = '';
      for (let i = 0; i < this.width; i++) {
        str += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(str);
      }
    }
  }
};
