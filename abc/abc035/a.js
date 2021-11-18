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
    let wh = lines[0].split(" ");
    let w = parseInt(wh[0], 10), h = parseInt(wh[1], 10);
    if (w/4 * 3 === h) {
        console.log("4:3");
    } else {
        console.log("16:9");
    }
});