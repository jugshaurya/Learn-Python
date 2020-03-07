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

function ans(n, arr) {
  l = 0;
  r = n - 1;

  let total = 0;
  lsum = arr[l];
  rsum = arr[r];

  while (l < r) {
    if (lsum == rsum) {
      mid_ele_count = r - l - 1;
      total += mid_ele_count + 1;
      l += 1;
      lsum += arr[l];
      r -= 1;
      rsum += arr[r];
    } else if (lsum > rsum) {
      r -= 1;
      rsum += arr[r];
    } else {
      // lsum <rsum
      l += 1;
      lsum += arr[l];
    }
  }
  return total;
}

function main(input) {
  let arr = input.split("\n");
  let t = parseInt(arr[0]);
  arr.splice(0, 1);
  while (t > 0) {
    let n = parseInt(arr[0].split(" ")[0]);
    let aarr = arr[1].split(" ");
    let sarr = [];
    for (let i = 0; i < n; i++) {
      sarr.push(parseInt(aarr[i]));
    }
    console.log(ans(n, sarr));
    arr.splice(0, 2);
    t--;
  }
}
