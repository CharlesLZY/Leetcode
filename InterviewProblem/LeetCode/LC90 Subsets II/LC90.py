'''
Leetcode 90. Subsets II

Description:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# @param nums List[int] 
# @return List[List[int]]

### Backtrack Solution
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []
        def DFS(path, idx):
            ans.append(path[:]) ### trick
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    DFS(path, i+1)
                    path.pop()
        DFS([], 0)
        return ans
        