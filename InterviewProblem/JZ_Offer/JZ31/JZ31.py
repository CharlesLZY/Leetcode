'''
JZ31 栈的压入、弹出序列

描述：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
popV 的所有数字均在 pushV里面出现过
pushV 的所有数字均不相同

input : [1,2,3,4,5]  [4,5,3,2,1]
output: True
可以通过 push(1)=>push(2)=>push(3)=>push(4)=>pop()=>push(5)=>pop()=>pop()=>pop()=>pop()
'''

# @param pushV List[int]
# @param popV List[int] 
# @return bool

'''
Simulate the push process and maintain the stack. When a number is pushed, check the popV wehther the number is popped immediately.
If any pop happened, check whether other value in popV can be popped from the stack 
'''

### TC: O(n) and SC: O(n)
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        j = 0
        for i in range(len(pushV)): ### We are simulating the push process, so we iterate through the pushV
            if pushV[i] == popV[j]:
                j += 1
                while len(stack) > 0 and stack[-1] == popV[j]: ### keep popping if possible
                    stack.pop()
                    j += 1
            else:
                stack.append(pushV[i])

        for i in range(len(stack)):
            if popV[j] == stack.pop():
                j += 1
            else:
                return False

        return True

