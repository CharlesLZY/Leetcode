
'''
Leetcode 78. Subsets

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# @param nums  List[int]
# @return List[List[int]]

class Solution:
    def subsets(self, nums):
        ans = []
        def forward(path, idx):
            if idx == len(nums):
                ans.append(path[:])
                return
            forward(path, idx+1) ### skip current number
            forward(path+[nums[idx]], idx+1)
        forward([], 0)
        return ans