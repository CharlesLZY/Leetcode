import sys


a = [1,2,3]
b = [1,2,4]
print(id(a[1]) == id(b[1])) ### small constant int is constant in the memory

c = None
d = True
print(id(None) == id(c))
print(d is True)

i = 1
print(type(i))
print(id(i) == id(a[0]))
print(sys.getsizeof(i))