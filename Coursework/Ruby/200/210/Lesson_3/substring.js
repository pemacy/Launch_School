// substring.js

var indexOf = (s1, s2) => {
  idx = null;
  s1Len = s1.length;
  for (i = 0; i < s1Len; i++) {
    if (s1[i] === s2[0]) {
      idx = i;
      for (j = 1; j < s2.length; j++) {
        if (s1[i + j] !== s2[j]) {
          idx = null;
        }
      }
      break;
    }
  }
  idx = idx ? idx : -1;
  console.log(idx);
}

var lastIndexOf = (s1, s2) => {
  idx = null;
  s1Len = s1.length;
  for (i = 0; i < s1Len; i++) {
    if (s1[i] === s2[0]) {
      idx = i;
      for (j = 1; j < s2.length; j++) {
        if (s1[i + j] !== s2[j]) {
          idx = null;
        }
      }
    }
  }
  idx = idx ? idx : -1;
  console.log(idx);

}

indexOf('Some strings', 's');      // 5
indexOf('Blue Whale', 'Whale');    // 5
indexOf('Blue Whale', 'Blute');    // -1
indexOf('Blue Whale', 'leB');      // -1

lastIndexOf('Some strings', 's');                  // 11
lastIndexOf('Blue Whale, Killer Whale', 'Whale');  // 19
lastIndexOf('Blue Whale, Killer Whale', 'all');    // -1
