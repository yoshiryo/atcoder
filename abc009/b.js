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
    let dish = new Set();
    for (let i = 1; i <= n; i++) {
      dish.add(parseInt(lines[i], 10));
    }
    dish = Array.from(dish);
    dish.sort((a, b) => b - a);
    console.log(dish[1]);
});