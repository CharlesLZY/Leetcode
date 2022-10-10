import time
import os
import psutil

### generator is a function return a iterator
### generator' object is not subscriptable

def List(n=10000000):
    res = []
    for i in range(n):
        res.append(i)
    return res

def Generator(n=10000000):
    for i in range(n):
        yield i

start = time.perf_counter() ### get the most accurate timestamp that python can get

# test = [i for i in range(10000000)]
test = (i for i in range(10000000)) ### generator

end = time.perf_counter()

print(f"Time: {round(end-start, 1)}")

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss // 1024 // 1024}MB") ### in bytes


