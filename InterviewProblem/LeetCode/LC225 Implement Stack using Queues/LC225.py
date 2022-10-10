'''
Leetcode 225. Implement Stack using Queues

Description:
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support 
all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size 
and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list 
or deque (double-ended queue) as long as you use only a queue's standard operations.
'''

class MyStack:

    def __init__(self):
        self.queue = []

    '''

    |     |         |     |
    |  3  |         |  1  |     for i in range(len(self.queue)-1):
    |  1  |   -->   |  2  |         self.queue.append(self.queue.pop(0))
    |  2  |         |  3  |
    |—————|         |—————| 

     queue           queue

    '''

    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue)-1): ### remain the number we just appended
            self.queue.append(self.queue.pop(0))

        
    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0] ### since stack need to support top, stack should have peak function

    def empty(self):
        return len(self.queue) == 0



