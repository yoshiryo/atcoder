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
    let lh = lines[0].split(" ");
    let l = parseInt(lh[0], 10), h = parseInt(lh[1], 10);
    let n = parseInt(lines[1], 10);
    for (let i = 0; i < n; i++) {
        let a = parseInt(lines[i+2], 10);
        if (a < l) {
            console.log(l - a);
        } else if (h < a) {
            console.log(-1);
        } else {
            console.log(0);
        }
    }
});