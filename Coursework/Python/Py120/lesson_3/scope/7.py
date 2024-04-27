class Student:
    school_name = 'Oxford'
    def __init__(self, name):
        self.name = name
        print(self.__class__.school_name)

    def __str__(self):
        return F"{self.name} goes to the {self.school_name} School."

    @classmethod
    def school(cls):
        return cls.school_name

print(Student.school_name)
print(Student.school())
