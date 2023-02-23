// Write a function logMultiples that takes one argument number. It should log all multiples of the argument between 0 and 100 (inclusive) that are also odd numbers. Log the values in descending order.

var logMultiples = function(n) {
  for (i = 100; i >= n; i--) {
    if (i % 2 != 0 && i % n == 0) {
      console.log(i);
    }
  }
}

// logMultiples(17);


var logMult2 = function(n) {
  var highestMult = Math.floor(100 / n) * n;
  for (i = highestMult; i > 0; i -= n) {
    if (i % 2 == 1) {
      console.log(i);
    }
  }
}

logMult2(17);
