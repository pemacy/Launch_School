principle = 1000.0
interest = 1.05
new_principle = principle

for i in list(range(5)):
    new_principle = new_principle * interest

print(f'After 5 years of ${principle:.2f} dollars, and {(interest - 1) * 100:.0f}% interest, you would have ${new_principle:.2f}')
