'''
Leetcode 155. Min Stack

Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
'''

'''
    |     |         |     |
    |     |         |     |
    |     |         |     |
    |  4  |         |  4  |
    |—————|         |—————|
     stack            min

    |     |         |     |
    |     |         |     |
    |  2  |         |  2  |
    |  4  |         |  4  |
    |—————|         |—————|
     stack            min

    |     |         |     |
    |  3  |         |  2  |
    |  2  |         |  2  |
    |  4  |         |  4  |
    |—————|         |—————|
     stack            min

    |  1  |         |  1  |
    |  3  |         |  2  |
    |  2  |         |  2  |
    |  4  |         |  4  |
    |—————|         |—————|
     stack            min

'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
    	self.stack.append(val)
    	if self.min:
    		self.min.append(min(self.min[-1], val)) ### this is a stack, the former min will always live longer than this node
    	else:
    		self.min.append(val)
        

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
    	return self.min[-1]