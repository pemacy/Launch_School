// Convert the person object into a nested array nestedPerson, containing the same key-value pairs.

let person = {
  title: 'Duke',
  name: 'Nukem',
  age: 33
};

// Expected output:
// [['title', 'Duke'], ['name', 'Nukem'], ['age', 33]]
let nestedPersonProp = Object.entries(person);
console.log(nestedPersonProp);

let nestedPerson = [];

for (let prop in person) {
  nestedPerson.push([prop, person[prop]]);
}

console.log(nestedPerson);
