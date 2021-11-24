'use strict';

const { COPYFILE_FICLONE } = require("constants");
const { compileFunction } = require("vm");

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
    let abc = lines[0].split(" ");
    let a = parseInt(abc[0], 10), b = parseInt(abc[1], 10), c = parseInt(abc[2], 10);
    for (let i = 1; i <= 100000; i++) {
        if (a <= i && i <= b) {
            if (i%c == 0) {
                console.log(i);
                process.exit();
            }
        }
    }
    console.log(-1);
});