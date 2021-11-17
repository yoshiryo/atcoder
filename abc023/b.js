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
    let s = lines[1];
    let a = "b";
    if (n === 1) {
      console.log(0);
      process.exit();
    }
    for (let i = 1; i <= n; i++) {
      if (i%3 === 1) {
        a = "a" + a + "c";
      } else if (i%3 === 2) {
        a = "c" + a + "a";
      } else {
        a = "b" + a + "b";
      }
      if (a === s) {
        console.log(i);
        process.exit();
      }
    }
    console.log(-1)
});