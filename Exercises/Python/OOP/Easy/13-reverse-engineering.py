'''
Write a class such that the following code prints the results indicated by the comments:
'''

class Transform:
    def __init__(self, text):
        self.text = text

    def uppercase(self):
        return self.text.upper()

    @classmethod
    def lowercase(self, text):
        return text.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz
