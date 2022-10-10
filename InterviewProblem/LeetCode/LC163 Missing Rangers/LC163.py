'''
Leetcode 163. Missing Ranges

Description:
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, 
and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b
'''

# @param nums List[int]
# @param lower int
# @param upper int
# @return List[str]

### TC: O(n) and SC: O(1)
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        def missingRange(low, high):
            if high <= low + 1:
                return []
            elif high == low+2:
                return [str(low+1)]
            else:
                return [str(low+1)+"->"+str(high-1)]

        p = lower-1 ### trick 
        ans = []
        for n in nums:
            ans += missingRange(p,n)
            p = n
        ans += missingRange(p, high+1)
        return ans