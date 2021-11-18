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
    let ans = 0;
    let word = new Array();
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== "+") {
            if (s[i] !== "*") {
                word.push(s[i]);
            }
        } else {
            if (word.indexOf("0") === -1) {
                ans += 1;
            }
            word = [];
        }
    }
    if (word.indexOf("0") === -1) {
        ans += 1;
    }
    console.log(ans);
});