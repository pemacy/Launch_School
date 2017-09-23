// pattern.js

var generatePattern = n => {
  var count = 1;
  var lastLine = '';
  var width;

  for (i = 1; i <= n; i++) {
    lastLine += String(i);
  }

  width = lastLine.length;

  do {
    var txt = '';
    for (i = 1; i <= count; i++) {
      txt += String(i);
    }
    stars = width - txt.length;
    for (i = 1; i <= stars; i++) {
      txt += '*';
    }
    console.log(txt);
    count++;
  } while (count <= n)
}

generatePattern(13);
generatePattern(9);
