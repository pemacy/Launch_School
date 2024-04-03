// substr2.js

var substring = (string, start, end) => {
  var sub = '';

  if (!(typeof start === 'number')) {
    return string;
  } else if (end === undefined || end >= string.length) {
    end = string.length;
  } else if (end < 0 || isNaN(end)) {
    end = 0;
  }

  firstIdx = start < end ? start : end;
  len = Math.abs(start - end);
  lastIdx = firstIdx + len;

  for (var i = firstIdx; i < lastIdx; i++) {
    sub += string[i];
  }

  return sub;
}

var string = 'hello world';

console.log(substring(string, 2, 4));    // "ll"
console.log(substring(string, 4, 2));    // "ll"
console.log(substring(string, 0, -1));   // ""
console.log(substring(string, 2));       // "llo world"
console.log(substring(string, 'a'));     // "hello world"
console.log(substring(string, 8, 8));   // "rld"
console.log(substring(string, 8, 20));   // "rld"
