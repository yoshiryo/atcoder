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
    let x = parseInt(lines[2], 10);
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += parseInt(a[i], 10);
    }
    if (sum > x) {
        let cnt = 0;
        for (let i = 0; i < n; i++) {
            cnt += parseInt(a[i], 10);
            if (cnt > x) {
                console.log(i+1);
                process.exit();
            }
        }
    } else {
        let c = Math.floor(x/sum);
        let ans = BigInt(c*n);
        let cnt = 0;
        x -= sum*c;
        for (let i = 0; i < n; i++) {
            cnt += parseInt(a[i], 10);
            if (cnt > x) {
                let ANS = String(BigInt(i+1)+ans);
                a = ANS.split("n");
                console.log(a[0]);
                process.exit();
            }
        }
    }
});