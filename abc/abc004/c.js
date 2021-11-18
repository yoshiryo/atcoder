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
    let ans = [1, 2, 3, 4, 5, 6];
    let cnt = 0;
    let rem = n;
    while ( Math.floor(n/5) > 0) {
        let top = ans[0];
        ans.shift();
        ans.push(top);
        n -= 5;
        cnt += 1;
    }
    rem -= cnt*5;
    for (let i = 0; i < rem; i++) {
        [ans[i], ans[i+1]] = [ans[i+1], ans[i]];
    }
    console.log(ans.join(""));
});