import time
from datetime import datetime


# def display_time(t=datetime.now()):
#     print(t)

# print(display_time.__defaults__)
# display_time()
# time.sleep(1)
# display_time()
# time.sleep(1)


### if the default argument is mutable, it will be initialized when the function is defined
def add(x, array=[]):
    array.append(x)
    print(array)

add(1)
add(2)
add(3)