'''
Leetcode 152. Maximum Product Subarray

Description:
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''

# @param nums List[int]
# @return int

### Brute Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def maxProduct(self, nums):
        ans = nums[0]
        for i in range(len(nums)):
            res = 1
            for j in range(i, len(nums)):
                res = res * nums[j]
                ans = max(ans, res)
        return ans

### DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def maxProduct(self, nums):
        curMIN = [None]*len(nums) ### curMIN[i] means the min sub array product ends at i, curMIN[i] = min(nums[i], curMAX[i-1]*nums[i], curMIN[i-1]*nums[i])
        curMAX = [None]*len(nums) ### curMAX[i] means the max sub array product ends at i, curMAX[i] = max(nums[i], curMAX[i-1]*nums[i], curMIN[i-1]*nums[i])
        curMIN[0] = nums[0]
        curMAX[0] = nums[0]

        ans = nums[0]
        for i in range(1, len(nums)):
            curMIN[i] = min(nums[i], nums[i]*curMAX[i-1], nums[i]*curMIN[i-1])
            curMAX[i] = max(nums[i], nums[i]*curMAX[i-1], nums[i]*curMIN[i-1])
            ans = max(ans, curMAX[i])

        return ans

### One Pass Solution (Similar to LC53)
### TC: O(n) and SC: O(1)
class Solution:
    def maxProduct(self, nums):
        curMIN = nums[0]
        curMAX = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            tmp = curMAX ### key point, curMAX and curMIN must be updated simultaneously
            curMAX = max(nums[i], nums[i]*tmp, nums[i]*curMIN)
            curMIN = min(nums[i], nums[i]*tmp, nums[i]*curMIN) ### remain the largest negative value (give him a chance to meet another negative number)

            # curMAX, curMIN = max(nums[i], nums[i]*curMAX, nums[i]*curMIN), min(nums[i], nums[i]*curMAX, nums[i]*curMIN)
            
            ans = max(ans, curMAX)
        return ans