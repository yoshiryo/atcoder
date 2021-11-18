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
    let ans = [0, 0, 0, 0, 0, 0];
    let alpha = ["A", "B", "C", "D", "E", "F"];
    for (let i = 0; i < 6; i++) {
        let cnt = 0;
        for (let j = 0; j < s.length; j++) {
            if (alpha[i] === s[j]) {
                cnt += 1;
            }
        }
        ans[i] = cnt;
    }
    console.log(ans.join(" "));
});