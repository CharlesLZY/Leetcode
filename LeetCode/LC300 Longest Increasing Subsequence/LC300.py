'''
Leetcode 300. Longest Increasing Subsequence

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without 
changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''

# @param nums List[int] 
# @return int

### DP Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def lengthOfLIS(self, nums):
        DP_table = [1]*len(nums) ### DP[i] epresents the length of the longest increasing subsequence that ends at i
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP_table[i] = max(DP_table[i], DP_table[j]+1) ### DP[i] = max(DP[j]) + 1 where 0 <= j < i and nums[i] > nums[j]
        return max(DP_table)


### Stack Solution 
### TC: O(n^2) and SC: O(n) (TC can be optimized to O(nlogn))
class Solution:
    def lengthOfLIS(self, nums):
        stack = [nums[0]]
        '''
        The length remains correct because the length only changes when a new element is larger than any element in the stack. 
        In that case, the element is appended to the subsequence instead of replacing an existing element. 
        And the largest element in the stack will also be updated by new elements.
        '''
        for num in nums[1:]:
            if num > stack[-1]:
                stack.append(num)
            else:
                for i in range(len(stack)): ### can be optimized to binary search to find the first larger number
                    if stack[i] >= num:
                        stack[i] = num ### 太tricky了
                        break
        return len(stack)