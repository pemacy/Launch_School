'''
Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:
'''

def extract_language(local):
    return local.split('_')[0]

def extract_region(local):
    return local.split('_')[1][0:2]

def local_greet(local):
    language = extract_language(local)
    region = extract_region(local)

    greet = {
            'en': {
                'US': 'Hey',
                'GB': 'Hello',
                'AU': 'Howdy',
                },
            'fr': {
                'FR': 'Salut',
                'CA': 'Salut',
                'MA': 'Salut',
                },
            }
    return greet[language][region]

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

'''
Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, and feel free to fall back on the language-specific greetings in all other cases, for example:
'''

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

'''
When implementing local_greet, make sure you re-use your extract_language, extract_region, and greet functions from the previous exercises.

If you're interested, you can find a list of locales here.
'''
