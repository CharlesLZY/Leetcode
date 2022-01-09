'''
Leetcode 398. Random Pick Index

Description:
Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target. 
If there are multiple valid i's, then each index should have an equal probability of returning.
'''

import random

### Hash Table solution
### TC: O(N) and SC: O(N)
class Solution:
    def __init__(self, nums):
        self.hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in self.hashTable:
                self.hashTable[nums[i]] = [i]
            else:
                self.hashTable[nums[i]].append(i)

    def pick(self, target):
        index = self.hashTable[target]
        r = random.randint(0, len(index)-1)
        return index[r]


### Reservoir Sampling Solution
### TC: O(N) and SC: O(1)
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        count = 0
        idx = None
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randint(1, count) == count: ### for i it is 1/i chance to be selected and for idx it is 1-1/i chance to be replaced
                    idx = i
        ### If we pick the ith number, this implies that we do not pick any number further from index i+1 to n.
        ### i/i * (1-1/(i+1)) * (1-1/(i+2)) * (1-1/n) = 1/n
        return idx 
        