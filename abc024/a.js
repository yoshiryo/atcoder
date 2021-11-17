'use strict';
process.stdin.setEncoding("utf8");

var lines = []; 
var reader = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

reader.on("line", (line) => {
  lines.push(line);
});
reader.on("close", () => {
    //ここに処理を記述
    let abck = lines[0].split(" ");
    let a = parseInt(abck[0], 10), b = parseInt(abck[1], 10), c = parseInt(abck[2], 10), k = parseInt(abck[3], 10);
    let st = lines[1].split(" ");
    let s = parseInt(st[0], 10), t = parseInt(st[1], 10);
    let sum = a*s + b*t;
    if (s + t >= k) {
        console.log(sum - (s+t)*c);
    } else {
        console.log(sum);
    }
});