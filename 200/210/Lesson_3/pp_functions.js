/* pp_functions.js */

function ave(arr) {
  return sum(arr) / arr.length;
}

function sum(arr) {
  var total = 0;
  for (var i = 0, len = arr.length; i < len; i++) {
    total += arr[i];
  }
  return total
}

console.log(ave([4,5,6]));

var temperatures = [28, 45, 34, 56, 22, 37];
console.log(ave(temperatures));

