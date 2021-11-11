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
    let ans = "";
    let p = true;
    let cnt = 1
    let now = s[0];
    for (let i = 1; i < s.length; i++) {
        if (now === s[i]) {
            cnt += 1;
        } else {
            ans += now + String(cnt);
            now = s[i];
            cnt = 1;
        }
    }
    ans += now + String(cnt);
    console.log(ans);
});