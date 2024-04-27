class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    @classmethod
    def hi(cls):
        greet = Greeting()
        greet.greet('Hi')

    def hi(self):
        self.greet('Hello')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()
hello.hi()
