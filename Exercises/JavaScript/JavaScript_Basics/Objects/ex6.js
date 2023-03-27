// We are experimenting with some code to get more comfortable working with objects. Run the snippet below and explain why "It's true!" is never output.

let obj = {
  num: 42,
  'property name': 'string value',
  true: false,
  fun: function() {
    console.log('Harr Harr!');
  },
};

for (let prop in obj) {
  if (prop === true) {
    console.log("It's true!");
  }
}

// because the property true is converted to a string

console.log(Object.getOwnPropertyNames(obj));

for (let prop in obj) {
  console.log(`${prop} (${typeof prop})`);
}

// logs:
// num (string)
// property name (string)
// true (string)
// fun (string)

// In order for our code to log "It's true!", we need to compare obj's properties to 'true':

for (let prop in obj) {
  if (prop === 'true') {
    console.log("It's true!");
  }
}
