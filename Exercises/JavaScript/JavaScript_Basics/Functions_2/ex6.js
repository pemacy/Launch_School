// Create a function removeLastChar that takes a string as an argument, and returns the string without the last character.

removeLastChar('ciao!'); // 'ciao'
removeLastChar('hello'); // 'hell'

function removeLastChar(str) {
  console.log(str.substring(0,str.length-1));
}
