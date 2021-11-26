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
    let x = parseInt(lines[0], 10);
    if (0 <= x && x < 40) {
        console.log(40 - x);
    } else if (40 <= x && x < 70) {
        console.log(70 - x);
    } else if (70 <= x && x < 90) {
        console.log(90 - x);
    } else {
        console.log("expert");
    }
});