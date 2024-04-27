'''
Create a function that takes a string argument that consists entirely of
numeric digits and computes the greatest product of four consecutive digits in
the string. The argument will always have more than 4 digits.
'''

def greatest_product(s):
    # Problem:
    #   Input: string of digits
    #   Output: integer of greatest product of 4 consecutive digits
    #   Rules:
    #       compute products of all combinations of 4 consecutive digits
    #       return the greatest product
    #   Assumptions:
    #       argument passed will always be a string of at least 4 digits
    #   Edge Cases:
    #       empty string - no
    #       zero string - no
    #       max string size - no

    # Data Structure
    #   string with slicing
    #   list to store sums

    # Algorithm
    #   prods = []
    #   range 0 to len(s) - 4
    #       prods.appned prods [ int(l) for l in s[i: i + 3] ]
        # prod = 1
        # for n in [ int(l) for l in s[i:i + 4] ]:
        #     prod *= n
    #   return max prods

    prods = []
    for i in range(0, len(s) - 3):
        prod = 1
        for n in [ int(l) for l in s[i:i + 4] ]:
            prod *= n
        prods.append(prod)

    return max(prods)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
