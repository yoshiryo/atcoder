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
    let ad = lines[0].split(" ");
    let a = parseInt(ad[0], 10), d = parseInt(ad[1], 10);
    let ans = [(a+1) * d, a * (d+1)];
    ans.sort((a, b) => (b - a));
    console.log(ans[0]);
});