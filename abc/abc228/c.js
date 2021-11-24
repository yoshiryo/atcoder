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
    let nk = lines[0].split(" ");
    let n = parseInt(nk[0], 10), k = parseInt(nk[1], 10);
    let sum = new Array();
    let tem = new Array();
    for (let i = 0; i < n; i++) {
        let p = lines[i+1].split(" ");
        let p1 = parseInt(p[0], 10), p2 = parseInt(p[1], 10), p3 = parseInt(p[2], 10);
        sum.push(p1 + p2 + p3);
        tem.push(p1 + p2 + p3)
    }
    tem.sort((a, b) => (b - a));
    for (let i = 0; i < n; i++) {
        let now = sum[i];
        if (now > tem[k-1]) {
            console.log("Yes");
        } else {
            let diff = tem[k-1] - now;
            if (0 <= diff && diff <= 300) {
                console.log("Yes");
            } else {
                console.log("No");
            }
        }
    }
});