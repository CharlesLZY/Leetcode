'''
Leetcode 220. Contains Duplicate III

Description:
Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
'''

# @param nums List[int] 
# @param k int
# @param t int
# @return bool

'''
Bucket Sort:
Find the min and max is O(n). When we get the range of the data.
We can divide the range into k buckets.
We place each data in a bucket. And sort the bucket and concatenate the buckets.
'''

'''
The trick of this problem is to store num // t in the hash table, this way we can mark the 
open interval [num, num + t), but we still need to check the left neighbour interval and num+t
'''
### TC: O(n) and SC: O(k)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        hashTable = {}
        div = t if t > 0 else 1 ### corner case: t = 0
        for i in range(len(nums)):
            
            if nums[i] // div in hashTable:
                return True
            if nums[i] // div + 1 in hashTable:
                if hashTable[nums[i] // div + 1] - nums[i] == t: ### check the border of open interval
                    return True
            if nums[i] // div - 1 in hashTable:
                
                if hashTable[nums[i] // div - 1] - nums[i] >= -t: ### check left neighbour interval
                    return True
            hashTable[nums[i] // div] = nums[i]

            if i >= k:
                del hashTable[nums[i-k] // div]
        return False

