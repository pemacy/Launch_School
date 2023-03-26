// Change your isBlank function from the previous exercise to return true if the string is empty or only contains whitespace. For example:

isBlank('mars'); // false
isBlank('  ');   // true
isBlank('');     // true

function isBlank(str) {
  console.log(str.trim().length == 0);
}
