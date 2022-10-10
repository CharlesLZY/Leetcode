def foo(arg, *args, **kwargs):
    print(arg)
    print("args", args)
    print("kwargs", kwargs, kwargs.keys(), kwargs.values())

# foo(1,2,3,4,5, key1=1, key2=2)

arg = [1,2,3]
# foo(arg)
foo(*arg)

### 高阶函数(函数的函数)
def func():
    print("OK")
    
def ffunc(func):
    func()

# ffunc(func)

'''
Python内置的高阶函数: map, filter, sort
'''
# print(list(map(lambda x:x**2, [i for i in range(1, 11)])))
# print(list(filter(lambda x:x<6, [i for i in range(1, 11)])))

# arr = [-2,-1,3,-5,1,0]
# arr.sort(key=lambda x:abs(x))
# print(arr)