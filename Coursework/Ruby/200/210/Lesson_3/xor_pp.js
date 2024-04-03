// Write a function named isXor that takes two arguments, and returns true if exactly one argument is truthy, false otherwise. 

var isXor = function(a, b) {
  msg = Boolean(a) != Boolean(b);
  console.log(String(msg));
}

isXor(false, true);     // true
isXor(true, false);     // true
isXor(false, false);    // false
isXor(true, true);      // false


isXor(false, 3);        // true
isXor('a', undefined);  // true
isXor(null, '');        // false
isXor('2', 23);         // false
