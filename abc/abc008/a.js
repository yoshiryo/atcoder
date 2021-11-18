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
    let st = lines[0].split(" ");
    let s = parseInt(st[0], 10);
    let t = parseInt(st[1], 10);
    if (s === t) {
        console.log(1);
    } else {
        console.log(t - s + 1)
    }
});