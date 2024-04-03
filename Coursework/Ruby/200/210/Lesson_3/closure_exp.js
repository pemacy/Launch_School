function showName() {
  console.log(getName());
}
showName();
var name = 'Bob';
function getName() {
  return name;
}

function lunch() {
  food = 'tacos';
}
function menu() {
  console.log(food);
}
lunch();
console.log(food);

function outer() {
  function hello() {
    return 'hello world!';
  }

  return hello();
}

console.log(typeof hello);    // can't access a local scope from here

var foo = outer;              // assign the function to another variable
console.log(foo());                        // we can then use it to invoke the function
