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
    let x = parseInt(lines[0], 10);
    for (let i = 1; i < 1000; i++) {
        if (x === i*i*i*i) {
            console.log(i);
            process.exit();
        }
    }
});