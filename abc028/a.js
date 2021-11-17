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
    if (n < 60) {
        console.log("Bad");
    } else if (n < 90) {
        console.log("Good");
    } else if (n < 100) {
        console.log("Great");
    } else {
        console.log("Perfect");
    }
});