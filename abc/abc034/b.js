'use strict';

const { O_APPEND } = require("constants");

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
    let n = parseInt(lines[0], 10);
    if (n%2 === 0) {
        console.log(n - 1);
    } else {
        console.log(n + 1);
    }
});