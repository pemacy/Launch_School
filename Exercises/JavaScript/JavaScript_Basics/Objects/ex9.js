// Write code that does the reverse, starting from a nested array of pairs and building an object.

let nestedArray = [['title', 'Duke'], ['name', 'Nukem'], ['age', 33]];

// Expected output:
// { title: 'Duke', name: 'Nukem', age: 33 }

let array = Object.fromEntries(nestedArray);
console.log(array);

let obj = {};
for (let arr of nestedArray) {
  obj[arr[0]] = arr[1];
}

console.log(obj);
