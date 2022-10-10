'''
Leetcode 325. Maximum Size Subarray Sum Equals k

Description:
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. 
If there is not one, return 0 instead.
'''

# @param nums List[int]
# @param k int
# @return int


'''
Refer to LC560
sum(arr[i:j]) = sum(arr[:j]) - sum(arr[:i])
target = sum(arr[:j]) - sum(arr[:i])
complement = sum(arr[:j]) - target
If we use hash table to store all cumulative sums, we can check complement to target k in O(1) and we can achieve one pass iteration.
'''
### TC: O(n) and SC: O(n)
class Solution:
    def maxSubArrayLen(self, nums, k):
        hashTable = {0:-1} ### sum[:i] : i 
        ans = 0
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            if cur - k in hashTable:
                ans = max(ans, i-hashTable[cur - k])
            if cur not in hashTable:
                hashTable[cur] = i

        return ans