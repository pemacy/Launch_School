// goldbach.js

var isPrime = (n) => {
  if (n !== 2 && (n % 2 === 0 || n < 2)) {
    return false;
  }
  upperLim = Math.floor(Math.sqrt(n));
  var i = 3;
  for (; i <= upperLim; i += 2) {
    if (i % n === 0) {
      return false;
    }
  }
  return true
}

var checkGoldbach = (n) => {
  var count = 0;
  var i = 2;
  var goldbach = false;
  for (; i <= (n / 2); i++) {
    if (isPrime(i)) {
      for (j = 2; j < n; j++) {
        if (isPrime(j) && (i + j === n)) {
          goldbach = true
          console.log(String(i) + ' and ' + String(j));
        }
      }
    }
  }
  if (goldbach == false) {
    console.log(null);
  }
}

checkGoldbach(3);
checkGoldbach(4);
checkGoldbach(12);
/*  checkGoldbach(100);
  */


