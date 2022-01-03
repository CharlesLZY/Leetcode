'''
Leetcode 31. Next Permutation

Description:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''

# @param nums List[int] 
# @return None

'''
impossible case: 7 6 5 4 3 2 1
5 4 2 3 7 6 1 -> 5 4 2 6 7 3 1 -> 5 4 2 6 1 3 7
5 4 1 2 3 6 7 -> 5 4 1 2 3 7 6 -> 5 4 1 2 3 7 6
5 4 6 7 1 3 2 -> 5 4 6 7 2 3 1 -> 5 4 6 7 2 1 3

'''

### TC: O(n) and SC: O(1)
class Solution:
    def nextPermutation(self, nums):
        last_ascending = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                last_ascending = i
        if last_ascending == -1:
            nums.reverse()
        else:
            ### replace the last ascending number with min number larger than it
            pivot = nums[last_ascending]
            MIN = float("inf")
            MIN_idx = -1
            for i in range(last_ascending+1, len(nums)):
                if nums[i] > pivot:
                    if nums[i] <= MIN: ### trick: <= , we want the small number stay behind, e.g. testcase: [2,3,1,3,3]
                        MIN = nums[i]
                        MIN_idx = i
            nums[last_ascending], nums[MIN_idx] = nums[MIN_idx], nums[last_ascending]

            ### sort the remaining numbers
            ### the trick is that after we swap the last asccending number with its min substitute,
            ### the remaining numbers are descending, so we only need to reverse it

            i = last_ascending + 1
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

