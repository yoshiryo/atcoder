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
    let ans = 0;
    for (let i = 0; i < 12; i++) {
        let s = lines[i];
        for (let j = 0; j < s.length; j++) {
            if (s[j] === "r") {
                ans += 1;
                break;
            } 
        }
    }
    console.log(ans);
});