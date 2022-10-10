'''
Leetcode 238. Product of Array Except Self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

# @param nums List[int]
# @return List[int]

'''
The trick of this problem is without using the division operation.

'''

### Intuitive Solution
### TC: O(n) and SC: O(n)
class Solution:
    def productExceptSelf(self, nums):
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i]

        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i]

        ans = []
        for i in range(len(nums)):
            ans.append((prefix[i-1] if i-1 >= 0 else 1) * (suffix[i+1] if i < len(nums)-1 else 1))

        return ans

### Two Pass Solution
### TC: O(n) and SC: O(1)
class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        ### prefix is calculated

        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix * nums[i+1]
            ans[i] = ans[i] * suffix

        return ans