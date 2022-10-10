'''
Leetcode 179. Largest Number

Description:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''

# @param nums List[int] 
# @return str

### TC: O(nlogn) and SC: O(n)
class Solution:
    def largestNumber(self, nums):
        class uStr(str):
            def __lt__(self, other):
                return self+other > other+self

        ans = ''.join(sorted(map(str, nums), key=uStr))
        if ans[0] == '0': ### corner case: [0, 0]
            return '0'
        else:
            return ans