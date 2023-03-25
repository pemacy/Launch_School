// What will the following code log to the console and why? Don't run it until you have tried to answer.

function myFunction() {
  let a = 1;

  if (true) {
    console.log(a);
    let a = 2;
    console.log(a);
  }
}

myFunction();

// it will print a reference error because of the temporal dead zone created by the let definition
// unlike var, let hoists but causes the variable to not have a definition (which var defines as undefined)
