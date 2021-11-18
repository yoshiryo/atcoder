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
    let num = ["no", 0, 1, 0, 1, 1, 1, 0, 1, 0];
    let ans = 0
    for (let i = 0; i < n; i++) {
        let now = a[i];
        while (num[now] !== 0) {
            ans += 1;
            now -= 1;
        }
    }
    console.log(ans);
});