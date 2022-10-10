class Sample:
    attr_0 = 0
    num1 = 0 
    num2 = 0
    def __init__(self):
        self.attr_1 = 1
        self.num1 += 1 ### create a copy of this attribute for this instance
        Sample.num2 += 1
    
    def test(self):
        print(self.attr_0)
        print(self.attr_1)

a = Sample()
b = Sample()
# print(dir(a))
# print(Sample.__dict__) ### attr_0 can be found
# print(a.__dict__) ### attr_0 can not be found
# print(a.attr_0)
# Sample.attr_0 = 2
# print(a.attr_0)
# print(b.attr_0)
# a.attr_0 = 3 ### create an attribute for a instance (not the Sample class)
# print(a.__dict__) ### attr_0 can be found now

# print(a.num1, a.num2)
# print(b.num1, b.num2)
# print(Sample.num1, Sample.num2) ### num added twice

# class uStr(str):
#     def __lt__(self, other):
#         return self+other > other+self ### "7" < "3" < "30"

# a = uStr('3')
# b = uStr('7')
# c = uStr('30')
# print(sorted([a,b,c]))

class Base:
    attr_0 = 0
    def __init__(self):
        self.attr_1 = 1
    def foo(self, x):
        print("Base", self, x)
    def f(self):
        print("Base", self)

class Derived(Base):
    # def __init__(self):
    #     self.attr_1 = 1
    def foo(self, x):
        print("Derived", self, x)
        super().foo(x) # super(Derived, self).foo(x)
        print("Finished")

class DDerived(Derived):
    def f(self):
        print("DDerived", self)
        super().f()

# test = DDerived()
# test.foo(1)
# test.f()
# print(test.attr_0)
# Base.attr_0 += 1
# print(test.attr_0)
# print(Derived.__dict__)
# Derived.attr_0 += 1
# print(Derived.__dict__)
# print(Base.attr_0)


class Root:
    attr = "Root"
    def f(self):
        print("Root.f", self)

class A(Root):
    attr = "A"
    def f(self):
        print("A.f", self)
        super().f()
    
class B(Root):
    attr = "B"
    def f(self):
        print("B.f", self)
        # super().f()

class C(A, B): ### the relative order in the declaration is the order in the MRO, class D(A, C) will give an error
    def f(self, x):
        print("C.f", self, x)
        super().f()

'''
         -- Root --
        |          |
        A          B
        |          |
         --- C ----
'''
### Method Resolution Order(MRO)
# print(C.__mro__)

### super actually means "next in the MRO" not necessarily the parent
### In Python, MRO of any class starts from the class itself and eventually ends in the <class object>
### 如果要确保一定能跑到parent, 那么所有child都要加super

test = C()
# test.f("OK") ### C.f A.f B.f
# print(C.attr)

class Hi:
    def f(self):
        sup = super() ### returns a proxy object which is a super class
        print(sup)

class ProxyClass:
    def __init__(self, obj):
        self.obj = obj
    
    def __getattr__(self, item):
        return getattr(self.obj, item)

test = Hi()
# test.f()

# print(getattr(test, "f"))
# help(getattr)

# obj = [1,2,3]
# proxy = ProxyClass(obj)
# proxy.append(4)
# print(obj)
# print(proxy)

'''
Python里面所有class本身都是type class, 这和class的继承关系是两个话题, 所有class都继承自object
'''
# print(test.__class__)
# print(test.__class__.__class__)
# print(test.__class__.__class__.__mro__)

'''
Python中类的构造函数不是__init__()而是__new__()
'''

class Test:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('__init__')

# test = Test()

def foo(*args):
    print("OK", args)

### type class is a metaclass in Python
### metaclass can be considered as the class of class
A = type("A", (), {"foo":foo, "attr": 0})
# print(A.__name__)
# print(A.__class__)
# A.foo()

# a = A()
# print(a.__class__)
# a.foo()

B = type("B", (A,), {}) ### (A) is not tuple, but (A,) is tuple
print(B.__name__)
b = B()
print(b.attr)
print(B.__mro__)
