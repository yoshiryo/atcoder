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
    let nab = lines[0].split(" ");
    let n = parseInt(nab[0], 10), a = parseInt(nab[1], 10), b = parseInt(nab[2], 10);
    let wsum = 0, esum = 0;
    for (let i = 0; i < n; i++) {
        let sd = lines[i+1].split(" ");
        let s = sd[0], d = parseInt(sd[1], 10);
        if (s === "West") {
            if (d < a) {
                wsum += a;
            } else if (b < d) {
                wsum += b;
            } else {
                wsum += d;
            }
        } else {
            if (d < a) {
                esum += a;
            } else if (b < d) {
                esum += b;
            } else {
                esum += d;
            }
        }
    }
    if (wsum === esum) {
        console.log(0);
    } else if (wsum > esum) {
        console.log("West", wsum - esum);
    } else {
        console.log("East", esum - wsum);
    }
});