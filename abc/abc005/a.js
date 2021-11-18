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
    let xy = lines[0].split(" ");
    let x = parseInt(xy[0], 10);
    let y = parseInt(xy[1], 10);
    console.log(Math.floor(y/x));
});