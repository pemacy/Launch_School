/* Please predict the output of the following programs and explain why they output what they do.*/

/* =====================
 * Problem 1 
 * ===================== */
console.log('Problem 1');
function say() {
  if (false) {
    var a = 'hello from inside a block';
  }

  console.log(a);
}
say();

// would output undefined
// scoping in JS is function-level, not block level, so the hoisting would become
// function say() {
//    var a
//    if (false) { a = '...'; }
//    console.log(a);
// }


/* =====================
 * Problem 2 
 * ===================== */
console.log("\nProblem 2");

function hello() {
  a2 = 'hello';
  console.log(a2);

  if (false) {
    var a2 = 'hello again';
  }
}

hello();
// console.log(a2);

// output would be 'hello' followed by ReferenceError because var a2 is decared in the function


/* =====================
 * Problem 3 
 * ===================== */
console.log("\nProblem 3");

var a3 = 'hello';

for (var i = 0; i < 5; i++) {
  var a3 = i;
}

console.log(a3);

// output would be 4, scope is not block level, so the var a inside the for loop is redundant
// and would be ignored


/* =====================
 * Problem 4 
 * ===================== */
console.log("\nProblem 4");

var a4 = 1;

function foo() {
  a4 = 2;
  function bar() {
    a4 = 3;
    return 4;
  }

  return bar();
}

console.log(foo());
console.log(a4);

// output would be 4, then 3


/* =====================
 * Problem 5 
 * ===================== */
console.log("\nProblem 5");

var a5 = 'global';

function checkScope() {
  var a5 = 'local';
  function nested() {
    var a5 = 'nested';
    function supernested() {
      a5 = 'supernested';
      return a5;
    }

    return supernested();
  }

  return nested();
}

console.log(checkScope());    // supernested
console.log(a5);              // global


/* =====================
 * Problem 6 
 * ===================== */
console.log("\nProblem 6");

var a6 = 'outer';
var b6 = 'outer';

console.log(a6);   // outer
console.log(b6);   //outer
setScope(a6);
console.log(a6);   // outer
console.log(b6);   // inner

function setScope(foo) {
  foo = 'inner';
  b6 = 'inner';
}

var qux = 2
function foo7() {
  var qux = 1;
  bar7();
}

function bar7() {
  console.log(qux);
}

foo(); // logs 1;
