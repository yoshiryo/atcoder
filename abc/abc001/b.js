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
    let m = lines[0];
    let km = parseFloat(m, 10);
    km /= 1000;
    let vv = ""
    if (km < 0.1) {
        vv += "00";
    } else if (km < 1) {
        s = String(km);
        l = s.split(".");
        vv += "0";
        vv += l[1][0];
    } else if (km <= 5) {
        km *= 10;
        s = String(km);
        l = s.split(".");
        vv += l[0];
    } else if (km <= 30) {
        km += 50;
        s = String(km);
        l = s.split(".");
        vv += l[0];
    } else if (km <= 70) {
        km -= 30;
        km /= 5;
        km += 80;
        s = String(km);
        l = s.split(".");
        vv += l[0];
    } else {
        vv += "89";
    }
    console.log(vv)
});