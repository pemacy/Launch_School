// starts_with.js

var startsWith = (str, query) => {
  if (query.length > str.length) {
    return false;
  }

  for (var i = 0; i < query.length; i++) {
    if (str[i] !== query[i]) {
      return false;
    }
  }

  return true;
}

var str = 'We put comprehension and mastery above all else';
console.log(startsWith(str, 'We'));       // true
console.log(startsWith(str, 'We put'));   // true
console.log(startsWith(str, ''));         // true
console.log(startsWith(str, 'put'));      // false

var longerString = 'We put comprehension and mastery above all else!';
console.log(startsWith(str, longerString));      // false
