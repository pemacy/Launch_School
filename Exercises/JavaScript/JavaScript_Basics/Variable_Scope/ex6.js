// What will the following code log to the console and why? Don't run it until you have tried to answer.

let a = 5;
let b = false;

if (a > 4) {
  let b = true;
}

console.log(b);

// it will print false because 'b' is re-scoped by the let statement inside the if block, so outside the if block 'b' will remain the same value
