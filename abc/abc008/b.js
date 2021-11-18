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
    let array = new Array();
    for (let i = 1; i <= n; i++) {
        array.push(lines[i]);
    }
    let max = 0
    let ans = array[0];
    for (let i = 0; i < array.length; i++) {
        let cnt = 0;
        let now = array[i];
        for (let j = 0; j < array.length; j++) {
            if (array[i] === array[j]) {
                cnt += 1;
            }
        }
        if (cnt > max) {
            ans = now;
            max = cnt;
        }
    }
    console.log(ans);
});