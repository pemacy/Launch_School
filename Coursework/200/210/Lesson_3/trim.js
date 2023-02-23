// trim.js

var trim = function(s) {
  var len = s.length;
  var newStr = '';
  var letterArea = false;
  for (i = 0; i < len; i++) {
    if (letterArea) {
      newStr += s[i];
    } else {
      if (s[i] === ' ') {
        continue;
      } else {
        newStr += s[i];
        letterArea = true;
      }
    }
  }

  len = newStr.length;
  var endLetter

  for (i = len - 1; i >= 0; i--) {
    if (newStr[i] === ' ') {
      continue;
    } else {
      endLetter = i;
      break;
    }
  }

  s = '';
  for (i = 0; i <= endLetter; i++) {
    s += newStr[i];
  }

  return s;
}

var val = trim('   hello r   ');

console.log(val + "\n" + val.length);
