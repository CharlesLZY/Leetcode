'''
Leetcode 442. Find All Duplicates in an Array

Description:
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and 
each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
'''

# @param nums List[int]
# @return List[int]

'''
The trick of this problem is that all the integers of nums are in the range [1, len(array)], , we can use them as index.
'''
### TC: O(n) and SC: O(1)
class Solution:
    def findDuplicates(self, nums):
        ans = []
        i = 0
        while i < len(nums):
            if nums[i] == i + 1 or nums[i] == -1:
                i += 1
            else:
                if nums[i] == nums[nums[i]-1]: ### unless the number is in on its own seat, the while loop will keep swapping 
                    ans.append(nums[i])
                    nums[i] = -1 ### marked it was visited
                    i += 1
                else:
                    ### important 
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] ### the order of the assignment statement cannot exchange
        return ans

'''
How clever a head is to come up with such solution.
Another trick in this problem that, number will only appear once or twice and all numbers are positive. 
So we can use negative number to mark whether the number is visited. If we visit n, then array[n-1] should be negative array[n-1].
Negative number will not effect the absolute value.
'''
### TC: O(n) and SC: O(1)
class Solution:
    def findDuplicates(self, nums):
        ans = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                ans.append(n)
            else:
                nums[n - 1] = - nums[n - 1]
        return ans


### Another method which can record the repeat times
### TC: O(n) and SC: O(1)
class Solution:
    def findDuplicates(self , nums):
        ans = []
        L = len(nums)
        repeat = 1 ### repeat times
        for n in nums:
            N = (n-1) % L
            if (nums[N]-1) // L == repeat:
                ans.append(N+1)
            else:
                nums[N] = nums[N] + L 
        return ans