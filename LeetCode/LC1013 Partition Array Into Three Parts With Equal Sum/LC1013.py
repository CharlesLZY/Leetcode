'''
Leetcode 1013. Partition Array Into Three Parts With Equal Sum

Description:
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with 
(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
'''

# @param s str 
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        S = sum(arr)
        if S % 3 != 0:
            return False
        
        s = S / 3
        
        count = 0
        cur = 0
        for n in arr:
            cur += n
            if cur == s:
                count += 1
                cur = 0
        
        if count >= 3: ### case: 0 0 0 0
            return True