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
    let nx = lines[0].split(" ");
    let n = parseInt(nx[0], 10), x = parseInt(nx[1], 10);
    let a = lines[1].split(" ");
    let b = new Array(false);
    let now = x - 1;
    while (!b[now]){
        b[now] = true;
        now = a[now] - 1;
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (b[i]) {
            ans += 1;
        }
    }
    console.log(ans);
});