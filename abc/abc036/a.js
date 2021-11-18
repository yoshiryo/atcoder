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
    let ab = lines[0].split(" ");
    let a = parseInt(ab[0], 10), b = parseInt(ab[1], 10);
    if (b%a === 0) {
        console.log(b/a);
    } else {
        console.log(Math.floor(b/a) + 1);
    }
});