'''
Leetcode 219. Contains Duplicate II

Description:
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

# @param nums List[int] 
# @param k int 
# @return bool

### Brute Solution
### TC: O(nk) and SC: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)-1):
            for j in range(1,k+1):
                if i+j < len(nums):
                    if nums[i] == nums[i+j]:
                        return True
                else:
                    break

        return False


### Hash Table Solution
### TC: O(n) and SC: O(k)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        hashTable = set()
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return True
            hashTable.add(nums[i])
            if i >= k:
                hashTable.remove(nums[i-k])

        return False