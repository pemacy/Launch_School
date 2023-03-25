// What will the following code log to the console and why? Don't run it until you have tried to answer.

if (true) {
  let myValue = 20;
}

console.log(myValue);

// let is block scoped, so it will print a reference error because myValue isn't available outside the if block
