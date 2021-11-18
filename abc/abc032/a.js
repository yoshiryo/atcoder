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
    let a = parseInt(lines[0], 10);
    let b = parseInt(lines[1], 10);
    let n = parseInt(lines[2], 10);
    while (true) {
        if (n%a === 0 && n%b === 0) {
            console.log(n);
            break
        }
        n += 1;
    }
});