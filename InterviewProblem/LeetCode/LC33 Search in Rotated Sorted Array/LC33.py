'''
Leetcode 33. Search in Rotated Sorted Array

Description:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

### Leetcode version is different from JZ offer version. All values in array are unique.

# @param nums List[int]
# @param target int
# @return int

### Baseline Solution
class Solution:
    def search(self, nums, target):
        def findPivot():
            left = 0
            right = len(nums) - 1
            while left < right: ### pivot must exist, if left == right, then that position is the pivot
                '''
                THE MOST IMPORTANT TRICK
                '''
                if nums[left] < nums[right]: ### this if is the trick
                    return left
                mid = (left + right) // 2
                if nums[mid] < nums[left]: ### trick: only compare with left
                    right = mid ### while lp < rp and mid = (1p+rp)//2 implies rp > mid, so here we will not cause infite loop
                elif nums[mid] > nums[left]: ### trick: only compare with left
                    left = mid + 1
                else:
                    ### Another Trick
                    left += 1 ### can not use left = mid because lp may equal to mid
            return left

         def findPivot():
            left = 0
            right = len(nums) - 1
            while left < right: ### pivot must exist, if left == right, then that position is the pivot
                if nums[left] < nums[right]:
                    return left
                mid = (left + right) // 2
                if nums[mid] < nums[right]: 
                    right = mid
                elif nums[mid] > nums[right]: 
                    left = mid + 1
                else:
                    right -= 1
            return left

        def findPivot(): ### if all values in array are unique
            lp = 0
            rp = len(nums) - 1
            if nums[lp] <= nums[rp]:
                return nums[0]

            while lp <= rp:
                mid = (lp + rp) // 2
                if nums[mid] > nums[mid+1]:
                    return nums[mid + 1]
                if mid - 1 >= 0 and nums[mid-1] > nums[mid]:
                    return nums[mid]

                if nums[0] < nums[mid]: ### trick
                    lp = mid + 1
                else:
                    rp = mid - 1

        def findPivot(): ### if all values in array are unique
            left = 0
            right = len(nums) - 1
            if nums[left] <= nums[right]: ### the array is already sorted
                return 0

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1 ### trick
                if nums[left] > nums[mid]: ### the pivot may be missed, but we will stop at the number just before the pivot
                    right = mid - 1
                else: 
                    left = mid + 1
            


        def find(low, high):
            left = low
            right = high
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else: ### nums[mid] > target
                        right = mid - 1
            return -1

        r = findPivot()
        pivot = nums[r] ### the min of rotated array

        if target < pivot:
            return -1
        if r == 0:
            return find(0, len(nums) - 1)
        elif target >= nums[0]:
            return find(0, r-1)
        else:
            return find(r, len(nums)-1)


### One-Pass solution
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: ### mid in the left sorted array
                if target >= nums[left] and target < nums[mid]: ### target in the left half
                # if target > nums[right] and target < nums[mid]: ### sufficient but non-essential, it will miss non-rotated case
                    right = mid - 1
                else:
                    left = mid + 1
            else: ### mid in the right sorted array, which implies the array must be rotated
                if target <= nums[right] and target > nums[mid]: ### target in the right half
                # if target < nums[left] and target > nums[mid]:  ### equivalent
                    left = mid + 1
                else:
                    right = mid - 1
        return -1