import random
import threading
from threading import Thread
import multiprocessing
from queue import Queue ### Queue in Python is a thread-safe to get and put data

def display(msg):
    threadName = threading.current_thread().name
    processName = multiprocessing.current_process().name
    print(f"{processName}/{threadName}: {msg}")

### Producer
def produce_job(queue, n_jobs):
    global finished
    for i in range(1, n_jobs+1): ### produce N jobs
        val = random.randint(1, 100)
        queue.put(val)
        display(f"Producing {i}: {val}")
    finished = True
    display(f"Finished producing {n_jobs} jobs.")

### Consumer
def consume_job(queue):
    global finished
    counter = 0
    while True:
        if not queue.empty():
            counter += 1
            val = queue.get()
            display(f"Consuming {counter}: {val}")
        else:
            if finished == True:
                break
    display(f"Finished consuming {counter} jobs.")

n_jobs = 10
jobs = Queue()
finished = False

producer = Thread(target=produce_job, args=[jobs, n_jobs], daemon=True)
consumer1 = Thread(target=consume_job, args=[jobs], daemon=True)
consumer2 = Thread(target=consume_job, args=[jobs], daemon=True)

producer.start()
consumer1.start()
consumer2.start()

producer.join()
consumer1.join()
consumer2.join()

