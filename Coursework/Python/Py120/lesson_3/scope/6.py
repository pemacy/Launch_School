class Student:
    school_name = 'Oxford'
    def __init__(self, name):
        self.name = name
        print(self.__class__.school_name)

    def __str__(self):
        return F"{self.name} goes to the {self.school_name} School."

m = Student('Mike')
s = Student('Sue')

print(m)
print(s)
