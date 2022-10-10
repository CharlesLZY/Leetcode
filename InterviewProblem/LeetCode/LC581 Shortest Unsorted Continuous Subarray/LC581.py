'''
Leetcode 581. Shortest Unsorted Continuous Subarray

Description:
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example:
Input: nums = [2,6,4,8,10,9,15]
Output: 5  ([6, 4, 8, 10, 9])

'''

# @param nums List[int] 
# @return int

### Intuitive Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def findUnsortedSubarray(self, nums):
        copy = nums[:]
        copy.sort()

        lp = -1
        rp = -1
        for i in range(len(nums)): ### find the first un-consistent from left to right
            if nums[i] != copy[i]:
                lp = i 
                break

        for i in range(len(nums)-1, -1, -1): ### find the last un-consistent from right to left
            if nums[i] != copy[i]:
                rp = i 
                break

        return rp - lp + 1 if lp != rp else 0


### Monotonic Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def findUnsortedSubarray(self, nums):
        ### find the first unsorted number should be k-th smallest number
        stack = [0] ### maintain an ascending stack
        start = len(nums) ### k-th smallest number
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop()) ### find the index of the unsorted number
                '''
                一直pop,直到回到它应该在的位置
                '''
            stack.append(i)

        if start == len(nums): ### not found, the array is already sorted
            return 0

        ### find the last unsorted number should be k-th largest number
        stack = [len(nums)-1] ### maintain an descending stack storing the index
        end = 0
        for i in range(len(nums)-2, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop()) ### find the index of the unsorted number
            stack.append(i)
                                
        return end - start + 1 

### Another version (awkward)
class Solution:
    def findUnsortedSubarray(self, nums):
        ### find the first unsorted number should be k-th smallest number
        stack = [nums[0]] ### maintain an ascending stack storing the numbers
        start = float("inf") ### k-th smallest number
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                stack.append(nums[i])
            else:
                while stack and stack[-1] > nums[i]:
                    stack.pop()
                stack.append(nums[i])
                ### we need to find the smallest unsorted number's rank
                start = min(start, len(stack)) ### trick: stack is ascending, so len(stack) is the ascending rank of the number in the array we have iterated so far
                ### find
        if start == float("inf"): ### not found, the array is already sorted
            return 0

        ### find the last unsorted number should be k-th largest number
        stack = [nums[-1]] ### maintain an descending stack storing the numbers
        end = float("inf")
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= nums[i+1]:
                stack.append(nums[i])
            else:
                while stack and stack[-1] < nums[i]:
                    stack.pop()
                stack.append(nums[i])
                ### we need to find the largest unsorted number's rank
                end = min(end, len(stack)) ### trick: stack is descending, so len(stack) is the descending rank of the number in the array we have iterated so far
                
        return len(nums) - start + 1 - end + 1


'''
The last number which doesn't update curMAX from left to right must be the end position of unsorted numbers.
The last number which doesn't update curMIN from right to left must be the start position of unsorted numbers.
'''
### Two Loop Solution
### TC: O(n) and SC: O(1)
class Solution:
    def findUnsortedSubarray(self, nums):
        curMAX = nums[0]
        end = -1
        ### find the last descending number from left to right which must be the end position of unsorted numbers
        for i in range(1, len(nums)):
            if nums[i] >= curMAX: ### a sorted array will keep update curMAX
                curMAX = nums[i] ### unsorted number may still update array [2 6 4 8 10 9 15]
            else: ### the last number which can not updata current MAX must be the last unsorted number
                end = i 

        if end == -1:
            return 0

        curMIN = nums[-1]
        start = -1
        ### iterate backward
        ### find the last ascending number from right to left which must be the start position of unsorted numbers
        for i in range(len(nums)-2, -1, -1): 
            if nums[i] <= curMIN: ### a sorted array will keep update curMIN
                curMIN = nums[i]
            else: ### the last number which can not updata current MIN must be the last unsorted number
                start = i


        return end - start + 1