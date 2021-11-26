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
    let s1 = lines[0];
    let s2 = lines[1];
    let s3 = lines[2];
    let t = lines[3];
    let ans = "";
    for (let i = 0; i < t.length; i++) {
        if (t[i] === "1") {
            ans += s1;
        } else if (t[i] === "2") {
            ans += s2;
        } else {
            ans += s3;
        }
    }
    console.log(ans);
});