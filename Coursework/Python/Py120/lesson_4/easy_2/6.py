class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return F"I am a {self.te}"

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>
