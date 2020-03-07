// Sample code to perform I/O:
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function(input) {
  stdin_input += input; // Reading input from STDIN
});

process.stdin.on("end", function() {
  main(stdin_input);
});

function main(input) {
  let arr = input.split("\n");
  let t = parseInt(arr[0]);
  arr.splice(0, 1);
  // console.log(arr)
  while (t > 0) {
    let n = parseInt(arr[0].split(" ")[0]);
    let k = parseInt(arr[0].split(" ")[1]);
    let skillArr = arr[1].split(" ");
    let sarr = [];
    for (let i = 0; i < n; i++) {
      if (skillArr[i] != " ") {
        sarr.push(parseInt(skillArr[i]));
      }
    }

    sarr.sort(function(a, b) {
      return a - b;
    });
    m = sarr.length;
    mini = sarr[m - 1] - sarr[m - k];

    r = m - 2;
    l = m - k - 1;
    while (l >= 0) {
      diff = sarr[r] - sarr[l];
      mini = Math.min(mini, diff);
      l--;
      r--;
    }
    console.log(mini);
    arr.splice(0, 2);
    t--;
  }
}
