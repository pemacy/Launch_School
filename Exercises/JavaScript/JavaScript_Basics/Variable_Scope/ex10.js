// What will the following code log to the console and why? Don't run it until you have tried to answer.

const a = {
  firstName: 'John',
  lastName: 'Doe'
};

function myFunction() {
  a.firstName = 'Jane';
}

myFunction();

console.log(a);

// it will print 'Jane' because you can re-assign properties of an object a constant points to, but not the object a constant ponits to
// const values can be mutated, but the values that are pointing to can't
