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
    let x = lines[0];
    let alpha = ["A", "B", "C", "D", "E"];
    console.log(alpha.indexOf(x) + 1);
});