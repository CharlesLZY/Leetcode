'''
Leetcode 75. Sort Colors

Description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

# @param nums List[int] 
# @return None

'''
The trick of this problem is that there are only three colors (0,1,2.
We put 0 on the left, 2 on the right and 1 in the middle.
Maintain 3 pointers, lp is the rightmost boundary of 0, rp is the leftmost boundary of 1.
Iterate the array, if arr[i] == 0, swap with arr[lp], if arr[i] == 2, swap with arr[rp]
'''

### TC: O(n) and SC: O(1)
class Solution:
    def sortColors(self, nums):
        lp = 0 ### last 0's index
        rp = len(nums)-1 ### last 2's index
        cur = 0
        while cur <= rp: ### trick: cur <= rp
            if nums[cur] == 0:
                nums[lp], nums[cur] = nums[cur], nums[lp]
                lp += 1
                cur += 1
            elif nums[cur] == 2: ### trick: cur stays
                nums[rp], nums[cur] = nums[cur], nums[rp]
                rp -= 1 ### cur stays because we have not checked the number swapped to cur
            else:
                cur += 1