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
    let a = lines[0];
    let len = a.length
    let alpha = "abcdefghijklmnopqrstuvwxyz";
    if (len === 1) {
        if (a === "a") {
            console.log(-1);
            process.exit();
        } else {
            console.log(alpha[alpha.indexOf(a) - 1]);
            process.exit();
        }
    } else {
        console.log(a.slice(0, len - 1));
        process.exit()
    }
});