import time
from threading import Thread, Lock
from multiprocessing import Process, Value, Array

### just sleep
def pending(t=1):
    # print(f"Pending {t} sec")
    time.sleep(t)
    # print("Finished")
    return "Result"

### CPU busy job
def busy():
    i = 0
    for _ in range(10000000):
        i += 1

### closure for decorator
def time_used(func):
    start = time.perf_counter() ### get the most accurate timestamp that python can get
    func()
    end = time.perf_counter()
    print(f"{func.__name__} used time: {round(end-start, 1)}")

def single_thread_pending():
    for _ in range(5):
        pending()

def multi_thread_pending():
    threads = []
    for _ in range(5):    
        t = Thread(target = pending, args=[1], daemon=True) ### Daemon设置为子线程是否随主线程一起结束, 默认为False
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def single_thread_busy():
    for _ in range(5):
        busy()

def multi_thread_busy():
    threads = []
    for _ in range(5):    
        t = Thread(target = busy, daemon=True)
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

def multi_process_busy():
    processs = []
    for _ in range(5):    
        t = Process(target = busy, daemon=True)
        t.start()
        processs.append(t)
    for process in processs:
        process.join()
'''
由于GIL(Global Interpreter Lock)的存在, 一个Python进程同一时间只能执行一个线程
GIL的存在是因为CPython解释器的内存管理不是线程安全的(引用计数)
对于CPU密集型任务, 多线程还不如单线程, 但是Python多进程是有用的
但对于IO密集型任务(不需要CPU参与), 多线程是有用的(比如爬虫下载东西)
或者挂机等待型任务，多线程也是有用的
'''
# time_used(single_thread_pending)
# time_used(multi_thread_pending)
# time_used(single_thread_busy)
# time_used(multi_thread_busy)
# time_used(multi_process_busy)

class Foo:
    j = 0
    def __init__(self):
        self.i = 0
    
    def job(self):
        temp = self.i ### copy i to the register from memory
        temp += 1 ### i++
        time.sleep(0.002) ### trick
        self.i = temp ### copy i to the memory from register

    def atomic_job(self, lock):
        lock.acquire()
        temp = self.i ### copy i to the register from memory
        temp += 1 ### i++
        time.sleep(0.002) ### trick
        self.i = temp ### copy i to the memory from register
        lock.release()
    
    def foo_job(self):
        self.i += 1
        Foo.j += 1
    
def thread_unsafe():
    foo = Foo()
    thread_list = []
    for _ in range(1000):
        thread = Thread(target=foo.job)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("thread_unsafe:", foo.i)

def thread_safe():
    foo = Foo()
    thread_list = []
    lock = Lock()
    for _ in range(1000):
        thread = Thread(target=foo.atomic_job, args=[lock])
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("thread_safe:", foo.i)

# thread_unsafe()
# thread_safe()


def job(val):
    temp = val.value
    temp += 1
    time.sleep(0.002) ### trick
    val.value = temp

def atomic_job(val):
    with val.get_lock():
        temp = val.value
        temp += 1
        time.sleep(0.002) ### trick
        val.value = temp

def process_unsafe():
    shared_value = Value("i", 0)
    process_list = []
    for _ in range(1000):
        process = Process(target=job, args=[shared_value])
        process_list.append(process)
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    print("process_unsafe:", shared_value.value)

def process_safe():
    shared_value = Value("i", 0)
    process_list = []
    for _ in range(1000):
        process = Process(target=atomic_job, args=[shared_value])
        process_list.append(process)
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    print("process_unsafe:", shared_value.value)

# process_unsafe()
# process_safe()

def test_multiprocess():
    foo = Foo()
    process_list = []
    for _ in range(1000):
        process = Process(target=foo.job)
        process_list.append(process)
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()
    '''
    each process has its own foo, the variable foo is not shared
    foo in the main process will not be affected by the processes in the process_list
    '''
    print("main process:", foo.i, foo.j) ### 0

# test_multiprocess()

def multi_thread_sum(n=100000000): ### multi-thread can not accelerate cpu-busy job
    res = [] ### List.append() is thread-safe, we can use list to store the return value of multi-thread
    def job(a,b):
        s = 0
        for i in range(a,b+1):
            s += i
        res.append(s)
    
    thread1 = Thread(target=job, args=[1,n//2])
    thread2 = Thread(target=job, args=[n//2+1,n])
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(sum(res))

def multi_process_sum(n=100000000):
    ### we can not use a list to store return value, because each process will have its own variable copy
    ### we need to use a Value or Array
    shared_value = Value("d", 0) ### d: double
    shared_array = Array('d', [0,0]) ### array's length is fixed

    def job(a,b,val):
        s = 0
        for i in range(a,b+1):
            s += i
        with val.get_lock():
            val.value += s

    def job_with_return(a,b,idx):
        s = 0
        for i in range(a,b+1):
            s += i
        shared_array[idx] = s
    
    process1 = Process(target=job, args=[1,n//2, 0])
    process2 = Process(target=job, args=[n//2+1,n, 1])

    # process1 = Process(target=job_with_return, args=[1,n//2, 0])
    # process2 = Process(target=job_with_return, args=[n//2+1,n, 1])
    
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print(shared_value.value)
    # print(sum(shared_array))

time_used(multi_thread_sum)
time_used(multi_process_sum)


