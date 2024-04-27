class Student:
    school_name = 'Oxford'
    def __init__(self):
        print(self.__class__.school_name)

s = Student()
