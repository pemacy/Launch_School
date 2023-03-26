// Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

let str = 'launch school tech & talk';
let str2 = str.split(' ');
for( let i = 0; i < str2.length; i += 1 ) {
  str2[i] = str2[i][0].toUpperCase() + str2[i].slice(1);
}
console.log(str2.join(' '));
