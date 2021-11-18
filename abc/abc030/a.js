'use strict';

const { table } = require("console");

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
    let abcd = lines[0].split(" ");
    let a = parseInt(abcd[0], 10), b = parseInt(abcd[1], 10), c = parseInt(abcd[2], 10), d = parseInt(abcd[3], 10);
    let taka = b/a;
    let aoki = d/c;
    if (aoki === taka) {
      console.log("DRAW");
    } else if (aoki > taka) {
      console.log("AOKI");
    } else {
      console.log("TAKAHASHI");
    }
});