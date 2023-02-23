// split.js

var split = (str, delim) => {
  if (delim === undefined) {
    console.log('ERROR no delimiter');
    return;
  }

  var len = str.length;
  var txt = '';

  for (i = 0; i < len; i++) {
    if (str[i] === delim) {
      console.log(txt);
      txt = '';
    } else if (!delim) {
      console.log(str[i]);
    } else {
      txt += str[i];
    }
  }

  if (txt) {
    console.log(txt);
  }
}

split(';hello', '');

