'''
Leetcode 448. Find All Numbers Disappeared in an Array

Description:
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''

# @param nums List[int] 
# @return List[int]

### Intuitive Hash Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def findDisappearedNumbers(self, nums):
        hashTable = [0]*len(nums)
        for num in nums:
            hashTable[num-1] += 1
        ans = []
        for i in range(len(nums)):
            if hashTable[i] == 0:
                ans.append(i+1)
        return ans

### Inplace Solution (refer to JZ3)
### TC: O(n) and SC: O(1)
class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0: ### each index corresponds to a number
                nums[abs(nums[i])-1] = - nums[abs(nums[i])-1] ### use negative value to mark whether the number is visited
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans