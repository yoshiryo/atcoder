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
    let n = lines[0];
    let ans = new Set();
    ans.add(n[0]);
    ans.add(n[1]);
    ans.add(n[2]);
    ans.add(n[3]);
    if (ans.size === 1) {
        console.log("SAME");
    } else {
        console.log("DIFFERENT");
    }
});