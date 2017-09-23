var logOddNumbers = function(n) {
    for (i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            console.log(i);
        }
    }
    
}

logOddNumbers(19);

var logOddNumbers2 = function(n) {
  for (i = 1; i <= n; i += 2) {
    console.log(i);
  }
}

logOddNumbers2(19);
