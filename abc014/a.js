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
    let a = parseInt(lines[0], 10);
    let b = parseInt(lines[1], 10);
    if (a%b === 0) {
        console.log(0);
    } else {
        console.log(b - a%b);
    }
});