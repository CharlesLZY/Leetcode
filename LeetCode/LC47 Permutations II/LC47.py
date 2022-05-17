'''
Leetcode 47. Permutations II

Description:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

# @param nums List[int]
# @return List[List[int]]

from collections import Counter
'''
collections: High-performance container datatypes
Common Datatype: 
- dequeue(): list-like container with fast appends and pops on either end
- Counter(): dict subclass for counting hashable objects
- OrderedDict(): dict subclass that remembers the order entries were added
- defaultDict(): dict subclass that calls a factory function to supply missing values
'''
### Counter Solution
class Solution:
    def permuteUnique(self, nums):
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


### Sort Solution
class Solution:
    def permuteUnique(self, nums):
        nums.sort() ### sort the array first
        ans = []
        def forward(perm, resNums):
            if len(resNums) == 0:
                ans.append(perm[:])
            else:
                for i in range(len(resNums)):
                    if i > 0 and resNums[i] == resNums[i-1]: ### trim the duplicated branch
                        continue
                    else:
                        perm.append(resNums[i])
                        forward(perm, resNums[:i] + resNums[i+1:])
                        perm.pop()
        forward([], nums)
        return ans



        