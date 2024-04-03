/* Please predict the output of the following programs and explain why they output what they do.*/

/* =====================
 * Problem 1 
 * ===================== */
console.log('Problem 1');
var a = 'outer';

function testScope() {
  var a = 'inner';
  console.log(a);
}

console.log(a); // outer
testScope();    // inner
console.log(a); // outer


/* =====================
 * Problem 2 
 * ===================== */
console.log('');
console.log('Problem 2');
var a = 'outer';

function testScope() {
  a = 'inner';
  console.log(a);
}

console.log(a); // outer
testScope();    // inner
console.log(a); // inner

/* =====================
 * Problem 3 
 * ===================== */
console.log('');
console.log('Problem 3');
var basket = 'empty';

function goShopping() {
  function shop1() {
    basket = 'tv';
  }

  console.log(basket);

  function shop2() {
    basket = 'computer';
  }

  function shop3() {
    var basket = 'play station';
    console.log(basket);
  }

  shop1();
  shop2();
  shop3();

  console.log(basket);
}

goShopping(); // empty, play station, computer

/* =====================
 * Problem 4 
 * ===================== */
console.log('');
console.log('Problem 4');

function hello() {
  a = 'hello';
}

hello();
console.log(a); // output: hello


/* =====================
 * Problem 5 
 * ===================== */
console.log('');
console.log('Problem 5');
function hello() {
  var a1 = 'hello'
}

hello();
console.log(a1); // a1 is not defined

/* =====================
 * Problem 6 
 * ===================== */
console.log('');
console.log('Problem 6');

console.log(a2); // undefined

var a2 = 1;

// after hoisting, this code becomes
// var a2;
// console.log(a2);
// a2 = 1;

/* =====================
 * Problem 7 
 * ===================== */
console.log('');
console.log('Problem 7');

console.log(a3); // ReferenceError a3 is not defined

function hello() {
  a3 = 1;
}

// after hoisting this becomes
// function hello() { a3 = 1; }
// console.log(a3);

/* even though function hello is placed prior to the console.log statement, because you don't call it
 * variable a3 is never defeined. */
