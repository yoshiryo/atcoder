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
    let nq = lines[0].split(" ");
    let n = parseInt(nq[0], 10), q = parseInt(nq[1], 10);
    let a = new Array();
    for (let i = 0; i < n; i++) {
        a.push(0);
    }
    for (let i = 0; i < q; i++) {
        let lrt = lines[i+1].split(" ");
        let l = parseInt(lrt[0], 10), r = parseInt(lrt[1], 10), t = parseInt(lrt[2], 10);
        for (let j = l-1; j < r; j++) {
            a[j] = t;
        }
    }
    for (let i = 0; i < n; i++) {
        console.log(a[i]);
    }
});