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
    let nm = lines[0].split(" ");
    let n = parseInt(nm[0], 10), m = parseInt(nm[1], 10);
    let hour = (n % 12 / 12 + m / 60 / 12) * 360;
    let minute = m / 60 * 360;
    let res = Math.abs(hour - minute);
    res = Math.min(res, 360 - res);
    console.log(res);
});