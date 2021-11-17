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
    const permutation = (nums, k) => {
        let ans = []
        if (nums.length < k) {
            return []
        }
        if (k === 1) {
            for (let i = 0; i < nums.length; i++) {
                ans[i] = [nums[i]]
            }
        } else {
            for (let i = 0; i < nums.length; i++) {
                let parts = nums.slice(0)
                parts.splice(i, 1)[0]
                let row = permutation(parts, k - 1)
                for (let j = 0; j < row.length; j++) {
                    ans.push([nums[i]].concat(row[j]))
                }
            }
        }
        return ans;
    }
    let n = parseInt(lines[0], 10);
    let arr = permutation(['a', 'b', 'c'], n);
    console.log(arr)
});