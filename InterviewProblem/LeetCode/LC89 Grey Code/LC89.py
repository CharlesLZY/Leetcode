'''
Leetcode 89. Gray Code(格雷编码)

Description:
An n-bit gray code sequence is a sequence of 2n integers where:
- Every integer is in the inclusive range [0, 2^n - 1],
- The first integer is 0,
- An integer appears no more than once in the sequence,
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

Example:
Input: n = 2
Output: [0,1,3,2] (which is [00,01,11,10]) or [0, 2, 3, 1] (which is [00,10,11,01])
'''

# @param n int
# @return List[int]

'''
格雷码有很多构造方法，比较好记的一种是镜像法
n = 0 : 0

n = 1 : (0)0 
        -----
        (0)1

n = 2 : 0 0
        1 0
        ---
        1 1
        0 1

n = 3: 00 0
       10 0
       11 0
       01 0
       ----
       01 1
       11 1
       10 1
       00 1
'''
### TC: O(2^n) and SC: O(2^n)
class Solution:
    def grayCode(self, n):
        def helper(n):
            if n == 0:
                return [0]
            if n == 1:
                return [0,1]
            else:
                res = helper(n-1)
                res = res + res[::-1]
                for i in range(len(res)//2):
                    res[i] = int(res[i] * 2)
                for i in range(len(res)//2, len(res)):
                    res[i] = int(res[i] * 2 + 1)
                return res
        
        return helper(n)