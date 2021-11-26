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
    let x = lines[0];
    let n = parseInt(lines[1], 10);
    let alp = "abcdefghijklmnopqrstuvwxyz";
    let ans = new Array();
    for (let i = 0; i < n; i++) {
        let s = lines[i+2];
        let t = "";
        for (let j = 0; j < s.length; j++) {
            for (let k = 0; k < 26; k++) {
                if (s[j] === x[k]) {
                    t += alp[k];
                    break
                }
            }
        }
        ans.push([t, s]);
    }
    ans.sort();
    for (let i = 0; i < n; i++) {
        console.log(ans[i][1]);
    }
});