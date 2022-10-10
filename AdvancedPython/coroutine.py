import time

def job1():
    while True:
        print("job1")
        time.sleep(1)
        yield
        

def job2():
    while True:
        print("job2")
        time.sleep(1)
        yield

j1 = job1()
j2 = job2()



start = time.perf_counter() ### get the most accurate timestamp that python can get
for _ in range(5):
    next(j1)
    next(j2)
end = time.perf_counter()
print(f"Time: {round(end-start, 1)}")
