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
    let stx = lines[0].split(" ");
    let s = parseInt(stx[0], 10), t = parseInt(stx[1], 10), x = parseInt(stx[2], 10);
    if (s < t) {
        if (s <= x && x < t) {
            console.log("Yes");
        } else {
            console.log("No");
        }
    } else {
        if (x < t || s <= x) {
            console.log("Yes");
        } else {
            console.log("No");
        }
    }
});