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
    let t = lines[1];
    let card = ["a", "t", "c", "o", "d", "e", "r"];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === t[i]) {
            continue;
        } else {
            if (s[i] === "@") {
                if (card.indexOf(t[i]) === -1) {
                    console.log("You will lose");
                    process.exit();
                }
            } else if (t[i] === "@") {
                if (card.indexOf(s[i]) === -1) {
                    console.log("You will lose");
                    process.exit();
                }
            } else {
                console.log("You will lose");
                process.exit();
            }
        }
    }
    console.log("You can win")
});