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
    let x = lines[0];
    x = x.replace(/ch/g, "");
    x = x.replace(/o/g, "");
    x = x.replace(/k/g, "");
    x = x.replace(/u/g, "");
    if (x.length === 0) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});