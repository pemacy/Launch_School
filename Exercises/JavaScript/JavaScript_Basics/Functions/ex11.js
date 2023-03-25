// Building on your solutions from the previous exercises, write a function localGreet that takes a locale as input, and returns a greeting. The locale allows us to greet people from different countries differently also when they share the language, for example:

console.log(localGreet('en_US.UTF-8')); // 'Hey!'
console.log(localGreet('en_GB.UTF-8')); // 'Hello!'
console.log(localGreet('en_AU.UTF-8')); // 'Howdy!'

// Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, and feel free to fall back on the language-specific greetings in all other cases, for example:

console.log(localGreet('fr_FR.UTF-8')); // 'Salut!'
console.log(localGreet('fr_CA.UTF-8')); // 'Salut!'
console.log(localGreet('fr_MA.UTF-8')); // 'Salut!'

// When implementing localGreet, make sure to re-use your extractLanguage, extractRegion and greet functions from the previous exercises.

// (If you're interested, you can find a list of locales here: http://www.localeplanet.com/icu/iso639.html)

function localGreet(locale) {
  let lang = extractLanguage(locale);
  let region = extractRegion(locale);

  switch (lang) {
    case 'en': return enGreeting(region);
    case 'fr': return frGreeting(region);
  }
}

function extractLanguage(langCode) {
  return langCode.split('_')[0];
}

function extractRegion(str) {
  return str.split('_')[1].split('.')[0];
}

function enGreeting(region) {
  switch (region) {
    case 'US': return 'Hey!';
    case 'GB': return 'Hello';
    case 'AU': return 'Howdy!';
  }
}

function frGreeting(region) {
  region = region;
  return 'Salut!';
}
