pets = {
        'Cat': 'Meow',
        'Dog': 'Bark',
        'Bird': 'Tweet',
        }

print(f'Dogs make a {pets["Dog"]} sound')
print(f'There is no lizard mapping correct: {pets.get("Lizard")}')
print(f'There is no lizard mapping correct: {pets.get("Lizard", "<silence>")}')
