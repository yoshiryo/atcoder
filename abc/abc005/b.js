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
    let n = parseInt(lines[0], 10);
    let time = new Array();
    for (let i = 1; i <= n; i++) {
        time.push(parseInt(lines[i], 10));
    }
    console.log(time.sort((a, b) => a - b)[0]);
});