#!/usr/bin/node
const myVar = process.argv;
const myArr = [];

myVar.forEach((value, index) => {
  const i = parseInt(value);
  if (myVar.length > 2 && !isNaN(i)) {
    myArr.push(i);
  }
});
const tempArr = myArr.sort((a, b) => a - b);

if (tempArr.length === 0 || tempArr.length === 1) {
  console.log(0);
} else {
  console.log(tempArr[tempArr.length - 2]);
}