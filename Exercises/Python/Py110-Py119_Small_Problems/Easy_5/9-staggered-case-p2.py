'''
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.
'''

def staggered_case(s):
    new_s = ''
    s_case = 'u'
    for l in s:
        if not l.isalpha():
            new_s += l
        elif s_case == 'u':
            new_s += l.upper()
            s_case = 'l'
        else:
            new_s += l.lower()
            s_case = 'u'

    return new_s

print(staggered_case("I Love Launch School!") == "I lOvE lAuNcH sChOoL!")
print(staggered_case("ALL CAPS") == "AlL cApS")
print(staggered_case("ignore 77 the 444 numbers") == "IgNoRe 77 ThE 444 nUmBeRs")
