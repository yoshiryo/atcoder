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
    let flowers = new Array();
    for (let i = 0; i < n; i++) {
        let a = lines[i+1];
        flowers.push(a);
    }
    let ans = new Set(flowers);
    console.log(n - ans.size);
});