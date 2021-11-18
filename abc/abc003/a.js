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
    let N = lines[0];
    let n = parseInt(N, 10);
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        ans += 10000*i/n;
    }
    console.log(ans);
});