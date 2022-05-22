
'''
Leetcode 78. Subsets

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# @param nums  List[int]
# @return List[List[int]]

### A more general solution is in LC90

class Solution:
    def subsets(self, nums):
        ans = []
        def DFS(path, idx):
            if idx == len(nums):
                ans.append(path[:])
                return
            else:
                DFS(path, idx+1) ### skip current number
                DFS(path+[nums[idx]], idx+1)
        DFS([], 0)
        return ans