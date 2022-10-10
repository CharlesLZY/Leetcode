'''
Leetcode 46. Permutations

Description:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''

# @param nums List[int]
# @return List[List[int]]


'''
This problem is easy, all numbers are different.
'''
class Solution:
    def permute(self, nums):
        ans = []
        def forward(idx):
            if idx == len(nums):
                ans.append(nums[:])
            else:
                for i in range(idx, len(nums)): ### start from idx, because each number can choose to stay the same, not to swap
                    nums[i], nums[idx] = nums[idx], nums[i] ### swap
                    forward(idx+1)
                    nums[i], nums[idx] = nums[idx], nums[i] ### backtrack
        forward(0)
        return ans


### Counter Solution
from collections import Counter
class Solution:
    def permute(self, nums):
        ans = []
        def forward(perm, counter):
            if len(perm) == len(nums):
                ans.append(perm[:])
            else:
                for n in counter:
                    if counter[n] > 0: ### still can put in the permutation
                        perm.append(n)
                        counter[n] -= 1

                        forward(perm, counter)

                        perm.pop() ### backtrack
                        counter[n] += 1

        forward([], Counter(nums))
        return ans