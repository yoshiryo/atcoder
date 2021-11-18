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
    let a = parseInt(lines[0], 10);
    let b = parseInt(lines[1], 10);
    let c = parseInt(lines[2], 10);
    let ABC = [a, b, c];
    let abc = [a, b, c];
    abc.sort((a,b) => (b-a));
    let ans = [0, 0, 0];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++){
            if (abc[i] === ABC[j]) {
                ans.splice(j, 1, i+1);
            }
        }
    }
    for (let i = 0; i < 3; i++) {
        console.log(ans[i]);
    }
});