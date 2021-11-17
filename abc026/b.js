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
    let A = new Array();
    for (let i = 0; i < n; i++) {
        A.push(parseInt(lines[i+1]));
    }
    A.sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (i%2 === 0) {
            ans += A[i]*A[i];
        } else {
            ans -= A[i]*A[i];
        }
    }
    console.log(ans*Math.PI)
});