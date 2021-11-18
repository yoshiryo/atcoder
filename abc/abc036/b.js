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
    let S = new Array();
    for (let i = 0; i < n; i++) {
        let s = lines[i+1];
        S.push(s);
    }
    let ans = new Array();
    for (let i = 0; i < n; i++) {
        let word = ""
        for (let j = n-1; j >= 0; j--) {
            word += S[j][i];
        }
        ans.push(word);
    }
    for (let i = 0; i < n; i++) {
        console.log(ans[i]);
    }
});