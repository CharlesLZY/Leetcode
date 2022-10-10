'''
Leetcode 402. Remove K Digits

Description:
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
'''

# @param num str
# @param k int
# @return str

### Monotonic Stack
### TC: O(n) and SC: O(n)
class Solution:
    def removeKdigits(self, num, k):
        if k >= len(num): ### corner case
            return '0'
        if k == 0: ### corner case
            return num

        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k: ### trick
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k] ### at this time, stack is ascending, we just remove the last k digits

        while stack and stack[0] == '0':
            stack.pop(0)

        return ''.join(stack) if stack else '0'
















