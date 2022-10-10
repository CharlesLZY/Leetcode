'''
Leetcode 621. Task Scheduler

Description:
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''
# @param tasks List[str]
# @param n int
# @return int

'''
The intuition of this problem is that as long as we handle the most frequent task (which has to be seperated by the cooldown period),
we can just tile other tasks in all the mandatory cooldown period slot

Tasks: A B C D E A F A     n = 2
Most frequent tasks: A
A _ _ A _ _ A
A B C A D E A F

Tasks: A B A A B C A A     n = 2
A _ _ A _ _ A _ _ A _ _ A
A B C A B _ A _ _ A _ _ A

Tasks: A A A A B B B C C C  n = 1
A _ A _ A _ A
A B A C A B A C B C 
'''

### Heap Solution (explainable and understandable)
### TC: O(nlogn) and SC: O(n)
from collections import Counter
from heapq import * ### only supply min heap, we need to encapsulate our own max heap
class MAX_Heap:
    heap = [] ### min heap
    def __init__(self, array):
        for num in array:
            self.push(num) ### cannot use heapify, because we are implementing max heap
    def push(self, x):
        heappush(self.heap, -x)
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            return -heappop(self.heap)
    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return -self.heap[0]
    def __len__(self):
        return len(self.heap)

class Solution:
    def leastInterval(self, tasks, n):
        freqs = Counter(tasks)
        maxHeap = MAX_Heap([val for val in freqs.values()]) ### maintain a max heap to get the current most hurried task
        time = 0
        while len(maxHeap) > 0: ### maxHeap works as the remaining task to finish
            ### the slot is composed of the most hurried tasks (task which has the most time to be done) 
            ### and other less hurried tasks to fill the cooldown period 
            slot = [] 
            for i in range(n+1): ### a slot is supposed to be n+1 long where n is cooldown period
                if len(maxHeap) > 0: ### if we still have tasks not in the slot to put 
                    slot.append(maxHeap.pop()) ### always put the most hurried task, the task will be pop from the heap to maintain the cooldown period

            for task in slot:
                if task - 1 > 0: ### if the task still has to be executed after this execute, push it back to the max heap but update its time
                    maxHeap.push(task-1)

            if len(maxHeap) == 0: ### all tasks are done in this slot
                time += len(slot)
            else: ### still have tasks to finish, which implies the slot is full
                time += n+1
        return time

### Without the max heap we encapsulate
from heapq import * ### only supply min heap
class Solution:
    def leastInterval(self, tasks, n):
        freqs = Counter(tasks)
        maxHeap = [-val for val in freqs.values()] ### heapq only support min heap, so we have to use negative value to simualte the max heap
        heapify(maxHeap)
        time = 0
        while len(maxHeap) > 0:
            ### the slot is composed of the most hurried tasks (task which has the most time to be done) 
            ### and other less hurried tasks to fill the cooldown period 
            slot = [] 
            for i in range(n+1): ### the slot is supposed to be n+1 long
                if len(maxHeap) > 0: ### if we still have tasks not in the slot to put 
                    slot.append(heappop(maxHeap)) ### always put the most hurried task, the task will be pop from the heap to maintain the cooldown period

            for task in slot:
                if task + 1 < 0: ### we use negative value to simulate max heap
                    heappush(maxHeap, task+1) ### + 1 is equivalent to - 1 because we store negative number in the heap

            if len(maxHeap) == 0: ### all tasks are done in this slot
                time += len(slot)
            else: ### still have tasks to finish, which implies the slot is full
                time += n+1
        return time


### Another Solution need to be prove correctness
### TC: O(n) and SC: O(1)
class Solution:
    def leastInterval(self, tasks, n):
        freqs = [0]*26 ### the problem use A-Z as task name
        for task in tasks:
            freqs[ord(task) - ord('A')] += 1

        freqs.sort()

        '''
        tasks = [A A A B B B C] and n = 2
        
        A B C | A B _ | A B
        
        '''

        maxFreq = max(freqs)
        idleSlot = (maxFreq - 1) * (n+1)
        n_max = freqs.count(maxFreq) ### number of tasks have the same freq as A (the most frequent task)

        return max(len(tasks), idleSlot + n_max)
