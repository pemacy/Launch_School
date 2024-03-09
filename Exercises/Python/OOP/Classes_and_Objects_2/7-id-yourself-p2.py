'''
Update the following code so that it prints I'm Sophie! when it invokes print(kitty).
'''

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"I'm {self.name}!"

kitty= Cat('Sophie')
print(kitty)
