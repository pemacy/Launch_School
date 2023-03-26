// Given strings like the following, how can you check whether they're equal irrespective of whether the characters they contain are upper or lower case?

let string1 = 'Polar Bear';
let string2 = 'Polar bear';
let string3 = 'Penguin';

function compareWords(str1, str2) {
  return str1.toLowerCase() == str2.toLowerCase();
}
