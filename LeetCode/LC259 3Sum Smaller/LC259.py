'''
Leetcode 259. 3Sum Smaller

Description:
Given an array of n integers nums and an integer target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
'''

# @param nums List[int]
# @param target int 
# @return int

'''
找一共有多少对
'''
### Sub-problem: 2Sum Smaller
### Two Pointer Solution
def twoSumSmaller(nums, target):
    ans = 0
    nums.sort()
    lp = 0
    rp = len(nums)-1
    while lp < rp:
        temp = nums[lp] + nums[rp]
        if temp < target:
            ans += rp - lp ### trick: nums[lp] + any of nums[lp:rp] are smaller than target (the nums is sorted)
            lp += 1
        else:
            rp -= 1
    return ans

### Binary Search Solution
def twoSumSmaller(nums, target):
    def binarySearch(low, high, n): ### find the smallest number >= n
        lp = low
        rp = high

        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] < n:
                lp = mid + 1
            else:
                rp = mid ### mid = (lp + rp) // 2 and while lp < rp implies rp > mid, so this will not cause infinite loop
        return lp if nums[lp] >= n else -1

    nums.sort() ### binary search can only be applied to sorted array
    ans = 0

    lp = 0
    rp = len(nums)-1
    while lp < rp:
        pivot = nums[lp]
        boundary = binarySearch(lp+1, rp, target-pivot)
        if boundary == -1: ### nums[lp+1:rp] are all smaller than target-pivot
            ans += rp - lp ### don't mess up it is rp - lp
        else:
            ans += boundary - lp - 1
        
        lp += 1
        if boundary != -1: ### important !!!
            rp = boundary

    return ans

### Binary Search Solution
def twoSumSmaller(nums, target):
    def binarySearch(low, high, n): ### find the largest number < n
        lp = low
        rp = high

        while lp < rp:
            mid = (lp + rp) // 2 + 1 ### trick: ensure that mid > lp
            if nums[mid] < n:
                lp = mid ### trick: mid must be bigger than lp
            else:
                rp = mid - 1
        return rp if nums[rp] < n else -1

    nums.sort() ### binary search can only be applied to sorted array
    ans = 0

    lp = 0
    rp = len(nums)-1
    while lp < rp:
        pivot = nums[lp]
        boundary = binarySearch(lp+1, rp, target-pivot)

        if boundary != -1: 
            ans += boundary - lp
        else:
            break

        lp += 1
        rp = boundary

    return ans

### Two Pointer Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def threeSumSmaller(self, nums, target):
        def twoSumSmaller(start, target):
            ans = 0
            lp = start
            rp = len(nums)-1
            while lp < rp:
                temp = nums[lp] + nums[rp]
                if temp < target:
                    ans += rp - lp ### trick: nums[lp] + any of nums[lp:rp] are smaller than target (the nums is sorted)
                    lp += 1
                else:
                    rp -= 1
            return ans

        nums.sort()
        ans = 0

        for i in range(len(nums)-2):
            pivot = nums[i]
            ans += twoSumSmaller(i+1, target-pivot)

        return ans


### Binary Search Solution
### TC: O(n*nlogn) and SC: O(1)
class Solution:
    def threeSumSmaller(self, nums, target):
        def twoSumSmaller(start, target): ### the array should be sorted
            def binarySearch(low, high, n): ### find the smallest number >= n
                lp = low
                rp = high
                while lp < rp:
                    mid = (lp + rp) // 2
                    if nums[mid] < n:
                        lp = mid + 1
                    else:
                        rp = mid
                return lp if nums[lp] >= n else -1
            ans = 0
            lp = start
            rp = len(nums)-1
            while lp < rp:
                pivot = nums[lp]
                boundary = binarySearch(lp+1, rp, target-pivot)
                
                if boundary == -1: ### nums[lp+1:rp] are all smaller than target-pivot
                    ans += rp - lp
                else:
                    ans += boundary - lp - 1
                lp += 1
                if boundary != -1: ### important
                    rp = boundary
            return ans
        
        nums.sort()
        ans = 0

        for i in range(len(nums)-2):
            pivot = nums[i]
            res = target - pivot
            ans += twoSumSmaller(i+1, res)
        return ans

### Binary Search Solution
### TC: O(n*nlogn) and SC: O(1)
class Solution:
    def threeSumSmaller(self, nums, target):
        def twoSumSmaller(start, target): ### the array should be sorted
            ans = 0
            def binarySearch(low, high, n): ### find the largest number < n
                lp = low
                rp = high

                while lp < rp:
                    mid = (lp + rp) // 2 + 1 ### trick
                    if nums[mid] < n:
                        lp = mid
                    else:
                        rp = mid - 1
                return rp if nums[rp] < n else -1
            
            lp = start
            rp = len(nums)-1
            while lp < rp:
                pivot = nums[lp]
                boundary = binarySearch(lp+1, rp, target-pivot)
                if boundary != -1:
                    ans += boundary - lp
                else: ### there is no number smaller than target-pivot
                    break
                lp += 1
                rp = boundary
                
            return ans
        
        nums.sort()
        ans = 0

        for i in range(len(nums)-2):
            pivot = nums[i]
            res = target - pivot
            ans += twoSumSmaller(i+1, res)
        return ans

