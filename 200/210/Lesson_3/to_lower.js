// to_lower.js

var toLowerCase = str => {
  if (!(typeof str === 'string')) {
    return str;
  }

  var txt = '';
  var asciNum;

  for (var i = 0; i < str.length; i++) {
    asciNum = str.charCodeAt(i);
    
    if (str[i] >= 'A' && str[i] <= 'Z') {
      asciNum += 32;
    }

    txt += String.fromCharCode(asciNum);
  }

  return txt;
}

console.log(toLowerCase('ALPHABET'));      // "alphabet"
console.log(toLowerCase('123'));           // "123"
console.log(toLowerCase('abcDEF'));        // "abcdef"
