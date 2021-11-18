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
    let q = parseInt(lines[0], 10);
    if (q === 1) {
        console.log("ABC");
    } else {
        console.log("chokudai");
    }
});