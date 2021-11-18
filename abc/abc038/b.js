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
    let h1w1 = lines[0].split(" ");
    let h2w2 = lines[1].split(" ");
    let h1 = parseInt(h1w1[0], 10), w1 = parseInt(h1w1[1], 10);
    let h2 = parseInt(h2w2[0], 10), w2 = parseInt(h2w2[1], 10);
    if (h1 === h2 || h1 === w2 || w1 === h2 || w1 === w2) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});