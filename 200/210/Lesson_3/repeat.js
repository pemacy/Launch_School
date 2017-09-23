// repeat.js

var repeat = (str, n) => {
  var txt = '';
  if (typeof(n) !== 'number') {
    return undefined;
  } else if (n < 0) {
    return undefined;
  } else {
    for (var i = 0; i < n; i++) {
      txt += str;
    }
  }
  return txt;
}


console.log(repeat('abc', 1));       // "abc"
console.log(repeat('abc', 2));       // "abcabc"
console.log(repeat('abc', -1));      // undefined
console.log(repeat('abc', 0));       // ""
console.log(repeat('abc', 'a'));     // undefined
console.log(repeat('abc', false));   // undefined
console.log(repeat('abc', null));    // undefined
console.log(repeat('abc', '  '));    // undefined


// Launch School solution
var repeatLS = (str, times) => {
  var repeated = '';

  if isPositive(n) {
    return undefined;
  }

  for (var i = 0; i < n; i ++) {
    repeated += str;
  }
}

var isPositive = n => {
  return Number(n) === n && n >= 0;
}
