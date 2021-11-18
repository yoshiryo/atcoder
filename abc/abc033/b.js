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
    let SP = new Array();
    let sum = 0;
    for (let i = 0; i < n; i++) {
        let sp = lines[i+1].split(" ");
        let s = sp[0];
        let p = parseInt(sp[1], 10);
        sum += p;
        SP.push([s, p]);
    }
    for (let i = 0; i < n; i++) {
        if (sum/2 < SP[i][1]) {
            console.log(SP[i][0]);
            process.exit();
        }
    }
    console.log("atcoder");
});