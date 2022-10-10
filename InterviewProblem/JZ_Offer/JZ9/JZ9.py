'''
JZ9 用两个栈实现队列

描述：
用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。
队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素。
'''

### TC: Push - O(1) per operation, Pop - Amortized(On average) O(1) per operation
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
    
    ### stack 1 for push and stack 2 for pop (while stack 2 is empty, transfer node in stack 1 to stack 2)
    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        


### TC: Push - O(n) per operation, Pop - O(1) per operation
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

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

    def push(self, node):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(node)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
    def pop(self):
        node = self.stack1.pop()
        return node
