// Write code that stores all of the vehicle property names in an array called keys.

let vehicle = {
  manufacturer: 'Tesla',
  model: 'Model X',
  year: 2015,
  range: 295,
  seats: 7
};

let propKeys = Object.keys(vehicle);
console.log(propKeys);

let keys = [];

for (let prop in vehicle) {
  keys.push(prop);
}

console.log(keys);
