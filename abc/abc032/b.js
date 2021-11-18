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
    let s = lines[0];
    let k = parseInt(lines[1], 10);
    let ans = new Set();
    for (let i = 0; i <= s.length - k; i++) {
        ans.add(s.slice(i, i+k));
    }
    console.log(ans.size);
});