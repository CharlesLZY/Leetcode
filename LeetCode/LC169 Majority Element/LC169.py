'''
Leetcode 169. Majority Element

Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n // 2 times. 
You may assume that the majority element always exists in the array.
'''

# @param nums List[int]
# @return int

### Intuitive solutions: 1. Hash Table 2. Sort

'''
Candidate Solution:
If a number occupies more than half of the array, it can use the 'perish together' strategy to beat all other numbers.
'''
### TC: O(n) and SC: O(1)
class Solution:
    def majorityElement(self, nums):
        candidate = None
        vote = 0
        for n in nums:
            if vote == 0:
                candidate = n
                vote += 1
            else:
                if candidate == n:
                    vote += 1
                else:
                    vote -= 1

        '''
        Leetcode version does not need to check whether the condidate is the mode
        '''
        winCondition = len(nums) // 2
        k = 0
        for n in nums:
            if n == candidate:
                k += 1
            if k >= winCondition:
                return candidate

        return -1
