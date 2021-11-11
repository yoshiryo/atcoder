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
    let se1 = lines[0].split(" ");
    let se2 = lines[1].split(" ");
    let se3 = lines[2].split(" ");
    let ans = 0;
    ans += parseInt(se1[0], 10) * parseInt(se1[1], 10) / 10;
    ans += parseInt(se2[0], 10) * parseInt(se2[1], 10) / 10;
    ans += parseInt(se3[0], 10) * parseInt(se3[1], 10) / 10;
    console.log(ans);
});