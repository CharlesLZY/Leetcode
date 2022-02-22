'''
Leetcode 560. Subarray Sum Equals K

Description:
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

# @param nums List[int] 
# @param k int 
# @return int

'''
Check all sub-array:
for i in range(len(array)):
    for j in range(i+1, len(array)+1):
        subArray = array[i:j]
'''

### Brute Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        for i in range(len(nums)):
            curSum = 0 ### reuse cumulative sum
            for j in range(i, len(nums)):
                curSum += nums[j]
                if curSum == k:
                    ans += 1
        return ans

'''
sum(arr[i:j]) = sum(arr[:j]) - sum(arr[:i])
target = sum(arr[:j]) - sum(arr[:i])
complement = sum(arr[:j]) - target
If we use hash table to store all cumulative sums, we can check complement to target k in O(1) and we can achieve one pass iteration.
'''
### Hash Table Solution (Similar to LC1)
### TC: O(n) and SC: O(n)
class Solution:
    def subarraySum(self, nums, k):
        hashTable = {0:1} ### prefix sum : times it appeared
        ans = 0
        curSum = 0
        for num in nums:
            curSum += num
            if curSum - k in hashTable:
                ans += hashTable[curSum - k]
                '''
                curSum = sum(arr[:j])
                if curSum - k occurs twice, which means that there exists i_1 and i_2 that sum(arr[:i_1]) = sum(arr[:i_2]) = curSum - k
                we have sum(arr[i_1:j]) = sum(arr[:j]) - sum(arr[:i_1]) = k and sum(arr[i_2:j]) = sum(arr[:j]) - sum(arr[:i_2]) = k
                i_1:j and i_2:j are two subarrays, so the ans need to be added twice
                '''
            hashTable[curSum] = hashTable.get(curSum, 0) + 1 ### trick: store the number of times the same sum occurs 
        return ans

'''
k = 6

1 ...
{0:1} curSum = 1  curSum - k = -5

1 2...
{0:1, 1:1} curSum = 3  curSum - k = -3

1 2 3...
{0:1, 1:1, 3:1} curSum = 6  curSum - k = 0

1 2 3 -6... 
{0:1, 1:1, 3:1, 6:1} curSum = 0  curSum - k = -6

1 2 3 -6 6...
{0:2, 1:1, 3:1, 6:1} curSum = 6  curSum - k = 0

1 2 3 -6 6 6 ...
{0:2, 1:1, 3:1, 6:2} curSum = 12  curSum - k = 6

'''