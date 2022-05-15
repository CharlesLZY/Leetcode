'''
Leetcode 18. 4Sum

Description:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
'''

# @param nums List[int]
# @param target int
# @return List[List[int]]

### TC: O(n^(k-1)) and SC: O(n)
class Solution:
    def fourSum(self, nums, target):
        def kSum(start, target, k): ### nums should be sorted
            if k == 1: ### corner case
                if target in nums:
                    return [target]
                else:
                    return []

            def twoSum(start, target):
                ans = []
                lp = start
                rp = len(nums)-1
                while lp < rp:
                    temp = nums[lp] + nums[rp]
                    if temp == target:
                        ans.append([nums[lp], nums[rp]])
                        ### important: skip all repeated numbers
                        lp += 1
                        while nums[lp] == nums[lp-1] and lp < rp:
                            lp += 1
                        # while rp-1 >= 0 and nums[rp] == nums[rp-1]: ### not necessary, because lp will skip the duplicate value, rp will move on naturally
                        #     rp -= 1

                        ''' 
                        ### Another version
                        while lp < rp and nums[lp] == nums[lp+1]:
                            lp += 1
                        lp += 1
                        '''
                        

                    elif temp < target:
                        lp += 1
                    else:
                        rp -= 1

                return ans
            
            ans = []
            if k == 2:
                return twoSum(start, target)
            else:
                for i in range(start, len(nums)-k+1):
                    ### important: i > start
                    if i > start and nums[i] == nums[i-1]: ### trick: use the first one and skip the following numbers so that we can still use multiple same numbers
                        continue ### skip repeated numbers

                    for subset in kSum(i+1, target-nums[i], k-1):

                        ans.append([nums[i]] + subset)

            return ans

        ### sort the array first
        nums.sort()
        return kSum(0, target, 4)


