'''
Leetcode 718. Maximum Length of Repeated Subarray

Description:
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example:
Input:  nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3 ([3,2,1])
'''

# @param nums1 List[int]
# @param nums2 List[int]
# @return int

### Brute Force
### TC: O(n^3) and SC: O(n)
class Solution:
    def findLength(self, nums1, nums2):
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)): ### a lot of repeated comparsion here
                k = 0
                while i+k < len(nums1) and j+k < len(nums2) and nums1[i+k] == nums2[j+k]:
                    k += 1
                ans = max(ans, k)
        return ans

### Better Brute Force: Reduce repeated comparsion of nums[i] != nums[j]
### TC: O(n^3) and SC: O(n)
from collections import defaultdict
class Solution:
    def findLength(self, nums1, nums2):
        hash_table = defaultdict(list) ### num: positions in nums2
        for j in range(len(nums2)):
            hash_table[nums2[j]].append(j)

        ans = 0
        for i in range(len(nums1)):
            for j in hash_table[nums1[i]]:
                k = 0
                while i+k < len(nums1) and j+k < len(nums2) and nums1[i+k] == nums2[j+k]:
                    k += 1
                ans = max(ans, k)
        return ans

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def findLength(self, nums1, nums2):
        ans = 0
        ### DP[i][j] means the length of the common tail of nums1[:i] and nums2[:j]
        DP_table = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    DP_table[i+1][j+1] = DP_table[i][j]+1
                    ans = max(ans, DP_table[i+1][j+1])
        return ans
        