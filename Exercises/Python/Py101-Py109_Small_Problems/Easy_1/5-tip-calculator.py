'''
Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.
'''

'''
What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
'''

bill = float(input('What is the bill? '))
tip_percent = float(input('What is the tip percent? ')) / 100
tip_total = tip_percent * bill
bill_total = bill + tip_total

print(f'The tip is ${tip_total:.2f}')
print(f'The total is ${bill_total:.2f}')
