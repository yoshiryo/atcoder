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
    let abc = lines[0].split(" ");
    let a = parseInt(abc[0], 10), b = parseInt(abc[1], 10), c = parseInt(abc[2], 10);
    let ans = 0;
    ans += a*b*2;
    ans += a*c*2;
    ans += b*c*2;
    console.log(ans);
});