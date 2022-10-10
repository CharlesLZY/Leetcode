'''
JZ30 包含min函数的栈

描述：
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。
此栈包含的方法有：
push(value):将value压入栈中
pop():弹出栈顶元素
top():获取栈顶元素
min():获取栈中最小元素
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

### TC: O(1) and SC: O(n)
class Solution:

    stack = []
    MIN = []

    def push(self, node):
        if len(self.stack) == 0:
            self.MIN.append(node)
        else:
            self.MIN.append(min(node, self.MIN[-1]))
        self.stack.append(node)

    def pop(self):
        self.MIN.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.MIN[-1]