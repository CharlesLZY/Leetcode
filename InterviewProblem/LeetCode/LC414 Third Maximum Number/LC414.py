'''
Leetcode 414. Third Maximum Number

Description:
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
'''

# @param nums List[int] 
# @return int


### Intuitive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def thirdMax(self, nums):
        nums = set(nums) ### use set to find 3 maximums to achieve efficiency
        if len(nums) < 3: ### corner case
            return max(nums)

        MAX = max(nums)
        nums.remove(MAX) ### delete the first maximum

        MAX = max(nums)
        nums.remove(MAX) ### delete the second maximum

        return max(nums)

### Optimized Solution
### TC: O(n) and SC: O(1)
class Solution:
    def thirdMax(self, nums):
        maximums = set() ### maintain three maximums
        for n in nums:
            if len(maximums) < 3:
                maximums.add(n)
            else:
                if n not in maximums and n > min(maximums): ### trick
                    maximums.remove(min(maximums))
                    maximums.add(n)

        if len(maximums) < 3:
            return max(maximums)
        else:
            return min(maximums)