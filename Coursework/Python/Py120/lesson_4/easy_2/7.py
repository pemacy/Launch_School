class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # works - instances can call class methods
print(tv.model()) # works

print(Television.manufacturer()) # works
print(Television.model()) # doesn't work, classes can't call instance methods
