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
    let abcde = lines[0].split(" ");
    let ans = new Array();
    for (let i = 0; i < 3; i++) {
        for (let j = i+1; j < 4; j++) {
            for (let k = j+1; k < 5; k++) {
                let sum = parseInt(abcde[i], 10) + parseInt(abcde[j], 10) + parseInt(abcde[k], 10);
                ans.push(sum);
            }
        }
    }
    ans.sort((a, b) => (b - a));
    console.log(ans[2]);
});