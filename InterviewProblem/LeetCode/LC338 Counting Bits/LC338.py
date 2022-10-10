'''
Leetcode 338. Counting Bits

Description:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i. 

Example
Input: n = 5
Output: [0,1,1,2,1,2]
ans[0] : 0 0
ans[1] : 1 1
ans[2] : 2 10
ans[3] : 3 11
ans[4] : 4 100
ans[5] : 5 101
'''

# @param n int 
# @return List[int]

### Brute Solution
### TC: O(nlogn) and SC: O(1)
class Solution:
    def countBits(self, n):
        ans = []
        for i in range(n+1):
            count = 0
            while i:
                if i & 1: ### whether the last bit is 1 
                    count += 1
                i = i >> 1
            ans.append(count)
        return ans


'''
x      = 1001011101
x >> 1 = 100101110

DP[x] = DP[x >> 1] +  x & 1
'''
### DP Solution
### TC: O(n) and SC: O(1)
class Solution:
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(n+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans