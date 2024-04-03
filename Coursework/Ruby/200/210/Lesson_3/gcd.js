// gcd.js

var gcd = (n1, n2) => {
  var lower = n1 > n2 ? n2 : n1;
  var higher = n1 > n2 ? n1 : n2;
  while (lower !== 0) {
    var temp = lower;
    lower = higher % lower;
    higher = temp;
  }
  console.log(higher);
}

gcd(12, 4);   // 4
gcd(15, 10);  // 5
gcd(9, 2);    // 1
