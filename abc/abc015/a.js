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
    let a = lines[0];
    let b = lines[1];
    if (a.length > b.length) {
        console.log(a);
    } else {
        console.log(b);
    }
});