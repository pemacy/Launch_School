# ======================================
# self has access to:
#   instance varaibles
#   instance methods if there is not a class method defined further down
#       in the class definition
#   class variables if they are not shadowed by instance variables
#   class methods if there is not an instance method of the same name
#       defined further down in the class definition
# cls has access to:
#   class instance variables
#   class methods if an instance method is not defined further down the class
#       definition - then it will try and run the instance method and fail
#       because self is not passed to it (cls is passed which is incompatible)
# ======================================
class Test:
    cls_var = 'class var'

    # @classmethod
    # def my_class(cls):
    #     print(F"cls.instance_var: {cls.inst_var}")

    def __init__(self):
        self.inst_var = 'instance var'

    def init_cls_inst_var(self):
        self.cls_var = 'instance var'


    def print_class_var(self):
        print()
        print(F"self.class_var: {self.cls_var}")
        print(F"self.__class__.class_var: {self.__class__.cls_var}")
        print(F"Test.class_var: {Test.cls_var}")
        print(F"type(self).class_var: {type(self).cls_var}")

    def shadow_class_var(self):
        print()
        self.cls_var = 'Now I am an instance var'
        print(F"self.class_var: {self.cls_var}")
        print(F"self.__class__.class_var: {self.__class__.cls_var}")
        print(F"Test.class_var: {Test.cls_var}")
        print(F"type(self).class_var: {type(self).cls_var}")

    def define_instance_class_var(self):
        self.init_cls_inst_var()

    def run_class_method(self):
        print()
        print("Running a class method with self")
        self.class_mtd()

    @staticmethod
    @classmethod
    def no_cls():
        print("No Class")

    def class_mtd(self):
        print()
        print("Instance Method")
        print(F"self.inst_var: {self.inst_var}")

    @classmethod
    def class_mtd(cls):
        print("Class Method")
        print(F"cls.class_var: {cls.cls_var}")

# t = Test()
# t.class_mtd()
# t.__class__.class_mtd()
# t.run_class_method()
# t.print_class_var()
# t.shadow_class_var()
# Test.class_mtd()



# ======================================
# Inheritance
# super will bubble up and doesn't need to be called by all intermediate super
#   classes
# ======================================

class Test1:
    def __init__(self, name):
        self.name = name
        self.my_meth()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

class Test1_(Test1):
    pass

class Test1__(Test1_):
    pass

class Test1___(Test1__):
    def __init__(self):
        print(super())
        super().__init__('Hello')

    def my_meth(self):
        print("From inside Test1___ (bottom subcalss)")

t = Test1___()
print(t.name)
