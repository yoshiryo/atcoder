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
    let l = lines[0].split(" ");
    let txa = parseInt(l[0], 10), tya = parseInt(l[1], 10), txb = parseInt(l[2], 10), tyb = parseInt(l[3], 10), t = parseInt(l[4], 10), v = parseInt(l[5], 10);
    let n = parseInt(lines[1], 10);
    for (let i = 0; i < n; i++) {
        let xy = lines[i+2].split(" ");
        let x = parseInt(xy[0], 10);
        let y = parseInt(xy[1], 10);
        let d = 0;
        d += Math.sqrt((x - txa)*(x - txa) + (y - tya)*(y - tya));
        d += Math.sqrt((x - txb)*(x - txb) + (y - tyb)*(y - tyb));
        if (d <= t*v) {
            console.log("YES");
            process.exit();
        }
    }
    console.log("NO");
});