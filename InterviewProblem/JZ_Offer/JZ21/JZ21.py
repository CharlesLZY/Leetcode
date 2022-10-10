'''
JZ21 调整数组顺序使奇数位于偶数前面(一)

描述：
输入一个长度为 n 整数数组，数组里面不含有相同的元素，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# @param array List[int] 
# @return List[int]

### TC: O(n) and SC: O(n)
class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 ==0:
                even.append(array[i])
            else:
                odd.append(array[i])
        return odd + even


### TC: O(n^2) and SC: O(1)
class Solution:
    def reOrderArray(self, array):
        loc = -1 # last odd location
        for i in range(len(array)):
            if array[i] % 2 == 1: # odd
                odd = array[i]
                for j in range(i-1, loc, -1): ### trick: move from right to left to maintain the relative position
                    array[j+1] = array[j] ### shift all even numbers
                loc += 1
                array[loc] = odd
                
        return array


class Solution:
    def reOrderArray(self, array):
        loc = 0 
        for i in range(len(array)):
            if array[i] % 2 == 1: # odd
                odd = array[i]
                for j in range(i-1, loc-1, -1): ### trick: move from right to left to maintain the relative position
                    array[j+1] = array[j] ### shift all even numbers
                array[loc] = odd
                loc += 1
        return array