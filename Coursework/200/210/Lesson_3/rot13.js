// rot13.js

var rotateLower = chr => {
  if (chr <= 'm') {
    return String.fromCharCode(chr.charCodeAt(0) + 13);
  } else {
    return String.fromCharCode(chr.charCodeAt(0) - 13);
  }
}

var rotateUpper = chr => {
  if (chr <= 'M') {
    return String.fromCharCode(chr.charCodeAt(0) + 13);
  } else {
    return String.fromCharCode(chr.charCodeAt(0) - 13);
  }
}

var rot13 = str => {
  strLen = str.length;
  rotated = '';

  for (var i = 0; i < strLen; i++) {
    if (str[i] >= 'a' && str[i] <= 'z') {
      rotated += rotateLower(str[i]);
    } else if (str[i] >= 'A' && str[i] <= 'Z') {
      rotated += rotateUpper(str[i]);
    } else {
      rotated += str[i];
    }
  }

  return rotated;
}

console.log(rot13('Teachers open the door, but you must enter by yourself.'));

// logs:
// Grnpuref bcra gur qbbe, ohg lbh zhfg ragre ol lbhefrys.
