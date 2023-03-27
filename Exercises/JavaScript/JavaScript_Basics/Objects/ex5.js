// Before running any code, determine what difference there will be in the output of the two code snippets below (if any).

// snippet 1

let ocean = {};
let prefix = 'Indian';

ocean.prefix = 'Pacific';

console.log(ocean); // ?

// snippet 2

ocean = {};
prefix = 'Indian';

ocean[prefix] = 'Pacific';

console.log(ocean); // ?

// first snippet will print { prefix: 'Pacific' }
// second snippet will print { Indian: 'Pacific' }
