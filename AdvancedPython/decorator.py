### closure
### closure is a struct with functions and its environment
def outer_function_1(var=0):
    # var = 1 
    ### Python allows nested functions.
    ### The value of the local variable in the parent function can be used directly in the inner function, 
    ### but if you want to modify the value of the local variable in the parent function in the inner function, 
    ### you must use the keyword nonlocal to declare that the variable is bound to the nearest parent function.

    def inner_function():

        ### without these two lines, it will form a closure
        # nonlocal var 
        # var += 1 ### run this line without the line above, it will cause error
                   ### because the var is defined in the enclosing scope

        print(var) ### var will be a free variable: variable that is used locally, but defined in an enclosing scope.
    
    return inner_function ### free variable can be used without context

def outer_function_2(var):
    def inner_function():
        # print(id(var))
        # var = [] ### this line will ruin the closure
        var.append(1) ### this line will not (I guess that python will try to find the immutable varible in the namespace)
        print(id(var))

    return inner_function

# a = []
# print(id(a))
# func1 = outer_function_1()
# func1()
# func2 = outer_function_2(a)
# func2()


'''
Why we need closure?
1. If we have a method with a private variables.
   We want to be able to use the variable directly in other methods, 
   but we don't want to expose it directly.
   Closure will maintain this variable even if the method has been destoried.
2. When a behavior has happened, its context should be bound to it. 
   For example, online shopping scene, when customer finished the purchasement, the commodity information should not change anymore.

'''


def decorator_func(original_func):
    def wrapper_func():
        print(f'wrapper executed this before {original_func.__name__}')
        return original_func()
        # return 
    return wrapper_func


@decorator_func ### this is the same thing that display = decorator_func(display)
def display():
    print("display function ran")

# decorated_display = decorator_func(display)
# decorated_display()

# print(f"diplay.__name__ is {display.__name__} now.")
# display() ### the usage of decorator is to execute the wrapper function before execute the original function


class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func
    
    def __call__(self, *args, **kwargs):
        print(f'call methods executed this before {self.original_func.__name__}')
        return self.original_func(*args, **kwargs)

@decorator_class
def display_info(info):
    print(info)

# print(display_info.__class__) 
# display_info("OK")


### using decorator to calculate time
import time
class used_timed(object):
    def __init__(self, original_func):
        self.original_func = original_func
    
    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        res = self.original_func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{self.original_func.__name__} used time: {round(end-start, 1)}")
        return res

@used_timed
def idle():
    time.sleep(5)

# idle()