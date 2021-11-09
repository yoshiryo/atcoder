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
    let xy = lines[0].split(" ");
    let xa = xy[0];
    let ya = xy[1];
    let xb = xy[2];
    let yb = xy[3];
    let xc = xy[4];
    let yc = xy[5];

    s = Math.abs((xa - xc)*(yb - yc) - (xb - xc)*(ya - yc)) / 2;
    console.log(s);
});