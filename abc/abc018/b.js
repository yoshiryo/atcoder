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
    let len = s.length;
    let n = parseInt(lines[1], 10);
    let lrs = "";
    for (let i = 0; i < n; i++) {
        let lr = lines[i+2].split(" ");
        let l = parseInt(lr[0], 10);
        let r = parseInt(lr[1], 10);
        lrs = s.slice(l-1, r).split("").reverse().join("");
        s = s.slice(0, l-1) + lrs + s.slice(r, len);
    }
    console.log(s);
});