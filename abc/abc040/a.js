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
    let nx = lines[0].split(" ");
    let n = parseInt(nx[0], 10), x = parseInt(nx[1], 10);
    let ans = [x - 1, n - x];
    ans.sort((a, b) => (a - b));
    console.log(ans[0]);
});