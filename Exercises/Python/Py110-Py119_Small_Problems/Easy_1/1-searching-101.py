'''
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.
'''

from number_suffixes import num_with_suffix

lst = []
for i in range(1, 6):
    num = input(f'Enter {num_with_suffix(i)} number: ')
    lst.append(num)

last = input(f'Enter last number: ')

result = 'is' if last in lst else "isn't"
print(f'{last} {result} in {",".join(lst)}.')

'''
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.
'''

'''
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
'''
