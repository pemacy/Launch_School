// Loop over the elements of the array fish, logging each one. Terminate the loop immediately after logging the string 'Nemo'.

let fish = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce'];

for (let el of fish) {
  if (el == 'Nemo') {
    console.log(el);
    break;
  }
}
