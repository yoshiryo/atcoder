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
    let ans = new Array();
    for (let i = 0; i < lines.length; i++) {
        let c = lines[i].split(" ");
        ans.push([c[3], c[2], c[1], c[0]]);
    }
    console.log(ans[3].join(" "))
    console.log(ans[2].join(" "))
    console.log(ans[1].join(" "))
    console.log(ans[0].join(" "))
});