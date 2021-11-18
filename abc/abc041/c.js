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
    let a = lines[1].split(" ");
    let ans = new Array();
    for (let i = 0; i < n; i++) {
        ans.push([a[i], i+1]);
    }
    ans.sort((a, b) => (b[0]- a[0]));
    for (let i = 0; i < n; i++) {
        console.log(ans[i][1]);
    }
});