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
    let A = parseInt(lines[0], 10);
    let B = parseInt(lines[1], 10);
    let a = A, b = B;
    let red = 0, blue = 0;
    while (a !== b) {
        if (a + 1 === 10) {
            a = 0;
        } else {
            a += 1;
        }
        red += 1;
    }
    a = A, b = B;
    while (a !== b) {
        if (a - 1 === -1) {
            a = 9;
        } else {
            a -= 1;
        }
        blue += 1;
    }
    if (red < blue) {
        console.log(red);
    } else {
        console.log(blue);
    }
});