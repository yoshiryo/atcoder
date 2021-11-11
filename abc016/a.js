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
    let md = lines[0].split(" ");
    let m = parseInt(md[0], 10), d = parseInt(md[1], 10);
    if (m%d === 0) {
        console.log("YES");
    } else {
        console.log("NO");
    }
});