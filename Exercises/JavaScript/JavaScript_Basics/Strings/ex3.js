// Implement a function repeat that repeats an input string a given number of times, as shown in the example below; without using the pre-defined string method String.prototype.repeat().

function repeat(num, str) {
  let newStr = '';

  for(let i = 0; i < num; i += 1) {
    newStr += str;
  }
  console.log(newStr);
}

repeat(3, 'ha'); // 'hahaha'
