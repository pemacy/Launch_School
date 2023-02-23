// Write a function that iterates over the integers from 1 to 100, inclusive. For multiples of three, log "Fizz" to the console. For multiples of five, log "Buzz". For numbers which are multiples of both three and five, log "FizzBuzz". For all other numbers, log the number.

var fizzBuzz = function() {
  for (i = 1; i <= 100; i++) {
    var msg = i % 3 === 0 ? 'Fizz' : '';
    msg += i % 5 === 0 ? 'Buzz' : '';
    console.log(msg || i)
  }
}

fizzBuzz();
