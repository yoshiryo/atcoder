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
    let rem = 2025 - n;
    for (let i = 1; i <= 9; i++) {
        for (let j = 1; j <= 9; j++) {
            if (rem === i*j) {
                let ans = String(i) + " x " + String(j);
                console.log(ans);
            }
        }
    }
});