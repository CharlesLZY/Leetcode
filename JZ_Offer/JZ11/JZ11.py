'''
JZ11 旋转数组的最小数字

描述：
有一个长度为 n 的非降序数组，比如[1,2,3,4,5]，将它进行旋转，即把一个数组最开始的若干个元素搬到数组的末尾，
变成一个旋转数组，比如变成了[3,4,5,6,1,2]，或者[4,5,1,2,3]这样的。请问，给定这样一个旋转数组，求数组中的最小值。
'''

# @param rotateArray List[int]
# @return int

'''
The key point of Binary Search is what should the mid compare with and which side to choose.

这题的trick在于：和正常的binary search不一样，一般search问题都是给一个target，mid会和target去比，
如果相等就直接找到了，如果不相等，mid可以直接排除，所以left和right的更新是mid-1和mid+1。
但这题存在一些情况，我们无法判断该往那边走，所以left和right的更新情况要复杂一点。
'''

'''
只能用在找最小，如果用在找pivot，没法处理如果有相同数字
'''
### TC: O(logn) and SC: O(1)
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray) - 1

        while left < right: 
            if rotateArray[left] < rotateArray[right]: ### key point: if rotateArray[left] < rotateArray[right]: return left
                return rotateArray[left]

            mid = (left + right) // 2

            if rotateArray[mid] < rotateArray[right]: ### 5 6 1 2 3 4 
                right = mid ### The mid can be the min, so it should be remained.
            elif rotateArray[mid] > rotateArray[right]: ### 5 6 1
                left = mid + 1 ### In this case, the mid can be excluded.
            else: ###  1 1 0 1  / 0 1 1 1
                right -= 1  ### We can not tell which side to go. But, at least, the mid is the same as the right end, so the right end can be discarded. 

        return rotateArray[left]


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray) - 1

        while left < right: 
            if rotateArray[left] < rotateArray[right]: ### key point: if rotateArray[left] < rotateArray[right]: return left
                return rotateArray[left]

            mid = (left + right) // 2

            if rotateArray[mid] < rotateArray[left]: ### 5 6 1 2 3 4 
                right = mid ### The mid can be the min, so it should be remained.
            elif rotateArray[mid] > rotateArray[left]: ### 5 6 1
                left = mid + 1 ### In this case, the mid can be excluded.
            else: ###  1 1 0 1 / 1 0 1 1 1
                left += 1 ### We can not tell which side to go. But, at least, the mid is the same as the left end, so the left end can be discarded. 

        return rotateArray[left]



### awkward modification of LC33 official solution
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray) - 1

        while left < right: 

            if rotateArray[left] < rotateArray[right]: ### 1 0 1 1 1 -> 0 1 1 1
                return rotateArray[left]

            mid = (left + right) // 2

            if rotateArray[mid] < rotateArray[mid-1]: ### 9 1 (mid -1) will be -1
                return rotateArray[mid]

            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[left]:
                right = mid - 1
            else: # 1 0 1 1 1 / 1 1 1 0 1
                left += 1 

        return rotateArray[left]


