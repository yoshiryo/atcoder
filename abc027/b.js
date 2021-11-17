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
    let a = lines[1].split(" ");
    let sum = 0;
    for (let i = 0; i < n; i++) {
      sum += parseInt(a[i], 10);
    }
    if (sum%n === 0) {
      let num = sum/n;
      let l = 0, r = sum;
      let ans = 0;
      for (let i = 0; i < n-1; i++) { 
        l += parseInt(a[i], 10);
        r -= parseInt(a[i], 10);
        if (l === (i+1)*num) {
          continue;
        } else {
            ans += 1;
        }
      }
      console.log(ans);
    } else {
      console.log(-1);
    }
});