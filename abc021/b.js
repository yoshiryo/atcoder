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
    let ab = lines[1].split(" ");
    let a = ab[0], b = ab[1];
    let k = parseInt(lines[2], 10);
    let p = lines[3].split(" ");
    p.push(a);
    p.push(b);
    let ans = new Set(p);
    if (ans.size === k + 2) {
      console.log("YES");
    } else {
      console.log("NO");
    }
});