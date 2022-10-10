### generator is a function return a iterator
### generator' object is not subscriptable

# names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
# heros = ["Spiderman", "Superman", "Deadpool", "Batman"]
# identities = zip(names, heros)
# # print(list(identities))
# for identity in identities:
#     print(identity)

# test = range(10) ### iterable but not a iterator(lazy iterable only allow one-pass)

arr = [i for i in range(3)]
iterator = iter(arr)
print(iterator) ### iterator object
print(next(iterator))
print(next(iterator))
print(next(iterator))
# next(iterator) ### StopIteration error
print(next(iterator, "EOF")) ### set the end
print(next(iterator, "EOF")) ### set the end





### enumerate is just a fancy iterator
# def abc(): 
#     letters = ['a', 'b', 'c']
#     for letter in letters:
#         yield letter

# for i, letter in enumerate(abc()):
#     print(i, letter)