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
    let l = lines[0].split(" ");
    let l1 = parseInt(l[0], 10), l2 = parseInt(l[1], 10), l3 = parseInt(l[2], 10);
    if (l1 === l2) {
        console.log(l3);
    } else if (l1 === l3) {
        console.log(l2);
    } else {
        console.log(l1);
    }
});