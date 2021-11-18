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
    let min = 10000000;
    for (let a=1; a<=n; a++) {
      const b = Math.floor(n / a);
      const c = n % a;
      min = Math.min(min, Math.abs(a - b) + c);
    }
    console.log(min);
});