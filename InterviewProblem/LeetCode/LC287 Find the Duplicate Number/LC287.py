'''
Leetcode 287. Find the Duplicate Number

Description:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
'''

# @param nums List[int]
# @return int


'''
Negative Mark
'''
### TC: O(n) and SC: O(1)
class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] = -nums[abs(nums[i])]

'''
[2,4,3,1,1]
'''
### Linked List Cycle (Floyd's Tortoise and Hare)
### TC: O(n) and SC: O(1)
class Solution:
    def findDuplicate(self, nums):
        fast = nums[0]
        slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        ### find the entrance of the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast