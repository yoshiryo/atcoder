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
    let cnt = 0;
    let sum = 0;
    for (let i = 0; i < n; i++) {
        if (a[i] !== "0") {
            cnt += 1;
            sum += parseInt(a[i], 10);
        }
    }
    console.log(Math.ceil(sum/cnt));
});