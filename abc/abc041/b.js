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
    let [a, b, c] = lines[0].split(" ").map(BigInt);
    const mod = 1000000007n
    let ans = a * b % mod * c % mod
    ans = Number(ans)
    console.log(ans)
});