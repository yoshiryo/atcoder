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
    let s = lines[0];
    if (s[s.length - 1] === "T") {
        console.log("YES");
    } else {
        console.log("NO");
    }
});