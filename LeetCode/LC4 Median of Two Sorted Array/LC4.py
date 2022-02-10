'''
Leetcode Median of Two Sorted Arrays

Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

# @param nums1 List[int] 
# @param nums2 List[int] 
# @return float



'''
m = len(nums1)
n = len(nums2)
                            p1
nums1: _ _ _ leftMAX1 | rightMIN1 _ _ _
nums2: _ _ _ leftMAX2 | rightMIN2 _ _ _
                            p2
nums1: 1 3 5 | 7
nums2: 4 | 8 10 12 14  

nums1: 1 3 5 | 7
nums2: 4 | 8 10 12 

nums1: 1 3 |
nums2: 4 | 8 10 12 13

nums1: | 8 9 
nums2: 1 2 4 | 12 

rightMIN = arr[partition]
leftMAX = arr[partition-1]

if leftMAX_1 <= rightMIN_2 (which means nums1[:p1] <= nums2[p2:]) and leftMAX_2 <= rightMIN_1 (which means nums2[:p2] <= nums1[p1:])
and we have p1 + p2 = (m+n)//2 half of numbers
then we find the correct median partition

if m+n is odd: median = min(rightMIN1, rightMIN2)
else: median = ( min(rightMIN1, rightMIN2) + max(leftMAX1, rightMAX2) ) / 2 

if partition == len(arr), rightMIN = float(inf)
if partition == 0, leftMAX = float(-inf)
'''


### A more clear solution
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        if m > n: ### assume that nums1 is shorter than nums2 to avoid some trivial cases
            nums1, nums2, m, n = nums2, nums1, n, m

        lp = 0 
        ######## IMPORTANT ########
        rp = m ### the partition ranges from 0 to len(arr), so we use m instead of m-1
        ######## IMPORTANT ########
        
        while True: ### trick: the partion must exist
        ### while lp <= ro:
            p1 = (lp + rp)//2 ### partition for nums1
            p2 = (m + n)//2 - p1 ### partition for nums2 and we have p1 + p2 = (m + n)//2

            leftMAX_1 = nums1[p1-1] if p1 > 0 else float("-inf") ### trick: use inf to generalize corner cases
            rightMIN_1 = nums1[p1] if p1 < m else float("inf")

            leftMAX_2 = nums2[p2-1] if p2 > 0 else float("-inf")
            rightMIN_2 = nums2[p2] if p2 < n else float("inf")


            if leftMAX_1 <= rightMIN_2 and leftMAX_2 <= rightMIN_1: ### the partition is correct
                if (m+n) % 2 == 1:
                    return min(rightMIN_1, rightMIN_2)
                else:
                    return (max(leftMAX_1, leftMAX_2) + min(rightMIN_1, rightMIN_2)) / 2
            else:
                if leftMAX_1 > rightMIN_2: ### nums1: 7 | 8 9  nums2: 1  2 | 3
                    rp = p1 - 1
                else: ### leftMAX_2 > rightMIN_1 nums1: 1 | 2 3  nums2: 7  8 | 9
                    lp = p1 + 1



'''
m = len(nums1) and n = len(nums2)
Assume that m <= n, the problem is converted to find the partition in nums1 where the right_min located
Do binary search for nums1, right_min is larger than (m + n) // 2 numbers, so we compare nums1[mid] with nums2[ (m + n) // 2 - mid - 1]
nums1[mid] > nums1[:mid] (mid numbers)
if nums1[mid] > nums2[:(m + n) // 2 - mid], (which means nums1[mid] > nums2[(m + n) // 2 - mid - 1]), binary search go left
'''

### My ugly solution
### TC: O(log (m+n)) and SC: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        if m > n: ### assume that nums1 is shorter than nums2 to avoid some trivial cases
            nums1, nums2, m, n = nums2, nums1, n, m

        if m == 0: ### corner case
            if n % 2 == 0:
                return (nums2[n//2] + nums2[n//2-1]) / 2
            else:
                return nums2[n//2]
        
        half = (m + n) // 2
        lp = 0
        rp = m-1

        while lp <= rp:   
               
                                           #  mid                com
            mid = (lp + rp) // 2 ### nums1: [1,5,6] nums2: [1,2,3,7,8,9]
                                           #  mid                  com
                                 ### nums1: [1,5,6] nums2: [1,2,3,7,8,9,10]
                                            #  mid                  com
            complement = half - mid ### nums1: [1,5] nums2: [1,2,3,7,8,9]
                                            #  mid                com           
                                    ### nums1: [1,5] nums2: [1,2,3,7,8]


            if nums1[mid] < nums2[complement - 1]:
                lp = mid+1
            else:
                if nums1[mid] > nums2[complement] if complement < n else float("inf"): ### testcase [0,0] and [0,0]
                    rp = mid-1
                else: ### we found the right min
                    lp = rp = mid
                    break

        
        if rp == -1: ### all elements in nums1 are on the right side of right_min
        ### can not use lp == 0, testcase: [2] and [1,3]
            if m == n:
                return (nums1[0] + nums2[-1]) / 2
            else:
                if (m + n) % 2 == 1:
                    return nums2[half]
                else:
                    return (nums2[half] + nums2[half-1]) / 2
                    ### no need to use min(nums2[half], nums1[0]), lp == 0 will belong to general case

        elif lp == m: ### all elements in nums1 are on the left side of the right_min
            if m == n:
                return (nums1[-1] + nums2[0]) / 2
            else:
                if (m + n) % 2 == 1:
                    return nums2[half-m]
                else:
                    return (nums2[half-m] + max(nums2[half-m-1], nums1[-1])) / 2
                    ### must use max(nums2[half-m-1], nums1[-1]), testcase: [2] and [1,3,4]

        else: ### general case 1. lp > rp  2. we find the right_min lp == rp
            right_min = nums1[lp] if lp == rp else min(nums1[lp], nums2[half-lp]) ### testcase: [1,4] and [2,3]
            if (m + n) % 2 == 1:
                return right_min
            else:
                left_max = max(nums1[lp-1], nums2[half-lp-1]) if lp > 0 else nums2[half-lp-1] ### testcase: [1,2] and [-1,3]
                return (left_max + right_min) / 2
