// Write a function that takes a number argument, and returns true if the number is prime, false if it is not.

var checkPrime = function(n) {
  if (n % 2 === 0 || n < 2) {
    return false;
  }
  upperLim = Math.floor(Math.sqrt(n));
  console.log(upperLim);
  for (i = 3; i <= upperLim; i += 2) {
    if (i % n === 0) {
      return false;
    }
  }
  return true
}

console.log(checkPrime(17));
console.log(checkPrime(22));
