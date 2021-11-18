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
    function dfs(letters, pattern, N) {
        if (N === 0) {
          console.log(pattern.join(''))
          pattern.pop()
          return
        }
        for (let i = 0; i < letters.length; i++) {
          pattern.push(letters[i]);
          dfs(letters, pattern, N-1);
        }
        pattern.pop()
        return
    }
    let n = parseInt(lines[0], 10);
    let letters = ["a", "b", "c"];
    dfs(letters, [], n);
});