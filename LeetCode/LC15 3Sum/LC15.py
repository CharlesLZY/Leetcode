'''
Leetcode 15. 3Sum

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

# @param nums List[int] 
# @return List[List[int]]

### TC: O(n^2) and SC: O(1)
class Solution:
    def threeSum(self, nums):
        ans = []

        nums.sort() ### TC O(nlogn) will not affect the whole time complexity

        ### Since the array is sorted, we can use two pointers and convert the problem into two sum problem

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: ### Important: skip the duplicate target
                continue

            pivot = nums[i]
            target = 0 - pivot ### 3 sum = 0 in this problem

            lp = i+1
            rp = len(nums)-1
            while lp < rp:
                temp = nums[lp] + nums[rp]
                if temp == target:
                    ans.append([pivot, nums[lp], nums[rp]])
                    lp += 1
                    ### Key point: skip duplicate nums[lp] 
                    while nums[lp] == nums[lp-1] and lp < rp: ### 3 sum has the property that two numbers are settled, the third one is fixed
                        lp += 1 ### in this part, the target is settled, if the nums[lp] == nums[lp-1], nums[rp] will be fixed, so we need to skip duplicated nums[lp]
                    
                elif temp < target:
                    lp += 1
                else:
                    rp -= 1
        return ans

        