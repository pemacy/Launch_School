// substr.js

var substr = (string, start, length) => {
  var sub = '';
  var strLen = string.length - 1;
  start = start < 0 ? strLen + start : start;
  var endIdx = start + length;

  for (var i = start; i < endIdx; i++) {
    if (i > strLen) {
      break;
    } else {
      sub += string[i];
    }
  }
  return sub;
}

var string = 'hello world';

console.log(substr(string, 2, 4));     // "llo "
console.log(substr(string, -3, 2));    // "rl"
console.log(substr(string, 8, 20));    // "rld"
console.log(substr(string, 0, -20));   // ""
console.log(substr(string, 0, 0));     // ""

