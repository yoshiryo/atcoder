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
    let n = parseInt(lines[1], 10);
    let cnt = 0;
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            cnt += 1;
            if (cnt === n) {
                console.log(s[i] + s[j]);
                break;
            }

        }
    }
});