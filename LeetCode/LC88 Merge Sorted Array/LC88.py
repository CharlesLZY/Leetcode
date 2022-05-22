'''
Leetcode 88. Merge Sorted Array

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''

# @param nums1 List[int]
# @param m int
# @param nums2 List[int]
# @param n int
# @return None

'''
这题的nums1长度是m+n,难点在于如何做到SC = O(1)
'''

### Place the number in reverse order
### TC: O(n) and SC: O(1)
class Solution:
    def merge(self, nums1, m, nums2, n):
    	p1 = m-1
        p2 = n-1
        
        for i in range(n+m-1,-1,-1):
            if p2 < 0 : ### the left number in nums1 are all set
                break
            elif p1 < 0:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                if nums1[p1] <= nums2[p2]:
                    nums1[i] = nums2[p2]
                    p2 -= 1
                else:
                    nums1[i] = nums1[p1]
                    p1 -= 1