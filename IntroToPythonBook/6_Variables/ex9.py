obj = 'ABcd'
obj2 = obj
obj.upper()
print(obj)
obj = list(obj)
obj.pop()
obj[2] = 'X'
obj.sort()
set(obj)
obj = tuple(obj)
print(obj)
