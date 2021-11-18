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
    let hh = 0;
    let mm = 0;
    let ss = 0;
    while (Math.floor(n/3600) > 0) {
        n -= 3600;
        hh += 1;
    }
    while(Math.floor(n/60) > 0) {
        n -= 60;
        mm += 1;
    }
    function zeroPadding(NUM, LEN){
        return (Array(LEN).join('0') + NUM).slice(-LEN);
    }
    ss = n;
    let ans = zeroPadding(hh, 2) + ":" + zeroPadding(mm, 2) + ":" + zeroPadding(ss, 2);
    console.log(ans);
});