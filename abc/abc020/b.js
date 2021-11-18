'use strict';

const { SSL_OP_NETSCAPE_CA_DN_BUG } = require("constants");

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
    let ab = lines[0].split(" ").join("");
    console.log(parseInt(ab, 10) * 2);   
});