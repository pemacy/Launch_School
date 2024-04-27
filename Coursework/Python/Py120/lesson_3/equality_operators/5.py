class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def _return_int(self, other):
        return (isinstance(self.value, int) or self.value.isdigit()) \
                and \
                (isinstance(other, int) or other.isdigit())

    def _return_str(self, other):
        return (isinstance(self.value, str) and not self.value.isdigit()) \
                or \
                (isinstance(other, str) and other.isdigit())

    def __add__(self, other):
        if not isinstance(other, int) and not isinstance(other, str):
            return NotImplemented
        if self._return_int(other):
            return Silly(int(self.value) + int(other))
        return Silly(str(self.value) + str(other))

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)
