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
    let t = 'BWBWBW'
    let scale = ['F#', 'So', 'S#', 'La', 'L#', 'Si', 'Do', 'D#', 'Re', 'R#', 'Mi', 'Fa']
    let scaleNum = scale.length
 
    let ans;
    for(let i = 0; i < s.length; i++) {
        let u = s.substr(i, 6)
        if(u === t) {
            if(i % scaleNum === 0) i = scaleNum
            ans = scale[scaleNum - i]
            break
        }
    }
 
    console.log(ans)
});