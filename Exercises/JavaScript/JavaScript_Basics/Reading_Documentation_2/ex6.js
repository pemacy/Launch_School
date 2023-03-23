// The MDN page for Date lists two methods to get the year of a date.

let today = new Date();

console.log(today.getYear());
console.log(today.getFullYear());

// What is the difference between the two methods and which one should you use?
// getYear() returns years since 1900
// getFullYear() returns current year
