 // Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length, as in the following example:

compareByLength('patience', 'perseverance'); // -1
compareByLength('strength', 'dignity');      //  1
compareByLength('humor', 'grace');           //  0

function compareByLength(str1, str2) {
  if (str1.length < str2.length) {
    console.log("-1");
  } else if (str2.length < str1.length) {
    console.log("1");
  } else {
    console.log("0");
  }
}
