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
    let nt = lines[0].split(" ");
    let n = parseInt(nt[0], 10), t = parseInt(nt[1], 10);
    let now = parseInt(lines[1], 10);
    let ans = 0;
    for (let i = 1; i < n; i++) {
        let a = parseInt(lines[i+1],  10);
        if (now+t < a) {
            ans += t;
            now = a;
        } else {
            ans += a - now;
            now = a;
        }
    }
    console.log(ans + t);
});