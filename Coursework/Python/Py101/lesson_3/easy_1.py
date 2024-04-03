'''
1. Yes, it will raise an IndexError

2. my_str.endswith('?')

3. famous_words = 'seven years ago'
    'Four score ' + famous_words
    ''.join(['Four score and', famous_words])

4. munsters_description = "the Munsters are CREEPY and Spooky."
   munsters_description.capitalize() # => 'The munsters are creepy and spooky.'

5. munsters_description = "The Munsters are creepy and spooky."
    munsters_description.swapcase()

6.  str1 = "Few things in life are as important as house training your pet dinosaur."
    str2 = "Fred and Wilma have a pet dinosaur named Dino."

    str1.find('Dino') #=> -1
    str2.find('Dino') #=> 41

    str1.count('Dino') #=> 0
    str2.count('Dino') #=> 1

7. flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
    flintstones.append('Dino')

8. flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
    flintstones.extend(['Dino', 'Hoppy'])

9. advice = "Few things in life are as important as house training your pet dinosaur."
    advice[:advice.find('house')]

# Expected return value:
# => 'Few things in life are as important as '

10. advice = "Few things in life are as important as house training your pet dinosaur."
    advice.replace('important', 'urgent')
'''
