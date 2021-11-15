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
    let nst = lines[0].split(" ");
    let n = parseInt(nst[0], 10), s = parseInt(nst[1], 10), t = parseInt(nst[2], 10);
    let w = parseInt(lines[1], 10);
    let cnt = 0;
    if (w >= s && w <= t) {
        cnt += 1;
    }
    for (let i = 0; i < n-1; i++) {
        let a = parseInt(lines[i+2], 10);
        w += a;
        if (w >= s && w <= t) {
            cnt += 1;
        }
    }
    console.log(cnt);
});