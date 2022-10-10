'''
Leetcode232. Implement Queue using Stacks

Description：
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support 
all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, 
and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list 
or deque (double-ended queue) as long as you use only a stack's standard operations.
'''

### TC: Push - O(1) per operation, Pop - Amortized(On average) O(1) per operation
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x):
        if len(self.stack1) == 0:
            self.front = x;
        self.stack1.append(x)
    
    ### stack 1 for push and stack 2 for pop (while stack 2 is empty, transfer x in stack 1 to stack 2)
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self):
        if len(self.stack2) > 0:
            return self.stack2[-1]### since queue need to support peek, stack should have pop function
        else:
            return self.front

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


### TC: Push - O(n) per operation, Pop - O(1) per operation
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    '''
    Step 1:

    |     |         |     |
    |     |         |     |
    |  1  |   -->   |     |
    |  2  |         |     |
    |—————|         |—————|

    Stack1          Stack2

    Step 2:

    |     |         |     |
    |     |         |     |
    |     |   <--   |  2  |
    |  3  |         |  1  |
    |—————|         |—————|

    Stack1          Stack2
    
    After Push:

    |     |         |     |
    |  1  |         |     |
    |  2  |         |     |
    |  3  |         |     |
    |—————|         |—————|

    Stack1          Stack2

    '''

    def push(self, x):
        if len(self.stack1) == 0:
            self.front = x;
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
    def pop(self):
        x = self.stack1.pop()
        self.front = self.stack1[-1] if self.stack1 else None ### since queue need to support peek, stack should have pop function
        return x

    def peek(self):
        return self.front

    def empty(self):
        return len(self.stack1) == 0