'use strict';

const { strictEqual } = require("assert");

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
    let nx = lines[0].split(" ");
    let n = parseInt(nx[0], 10);
    let x = parseInt(nx[1], 10);
    let a = lines[1].split(" ");
    let ans = new Array();
    for (let i = 0; i < n; i++) {
        if (x & (1 << i)) {
            ans.push(a[i]);
        }
    }
    let sum  = function(arr) {
        let sum = 0;
        arr.forEach(function(elm) {
            sum += parseInt(elm, 10);
        });
        return sum;
    };
    console.log(sum(ans));
});