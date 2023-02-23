// Write a function that logs the integers from 1 to 100 (inclusive) that are multiples of either 3 or 5. If the number is divisible by both 3 and 5, append an "!" to the number.

var threeFive = function(a, b) {
  var three;
  var five;

  for (i = a; i <= b; i++) {
    three = i % 3 == 0;
    five = i % 5 == 0;

    if (three && five) {
      console.log(String(i) + '!');
    } else if (three || five) {
      console.log(String(i));
    }
  }
}

threeFive(20, 45);
