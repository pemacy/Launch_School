'''
Write a function that takes a string and returns an object containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
You may assume that the string will always contain at least one character.
'''

def letter_percentages(s):
    l_len = len(s)
    results = {
            'lowercase': 0,
            'uppercase': 0,
            'neither': 0,
            }
    for l in s:
        if l.islower():
            # update_results(results)
            results['lowercase'] += 1
        elif l.isupper():
            results['uppercase'] += 1
        else:
            results['neither'] += 1

    for key in results:
        results[key] = f'{results[key] / l_len * 100:.2f}'
    return results

print(letter_percentages('abCdef 123'))
# { 'lowercase': "50.00", 'uppercase': "10.00", 'neither': "40.00" }

print(letter_percentages('AbCd +Ef'))
# { 'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00" }

print(letter_percentages('123'))
# { 'lowercase': "0.00", 'uppercase': "0.00", 'neither': "100.00" }
