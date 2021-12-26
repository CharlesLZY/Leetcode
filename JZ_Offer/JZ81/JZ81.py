'''
JZ81 调整数组顺序使奇数位于偶数前面(二)

描述：
输入一个长度为 n 整数数组，数组里面可能含有相同的元素，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，对奇数和奇数，偶数和偶数之间的相对位置不做要求。
'''

# @param array List[int]
# @return List[int]

### One common TC O(n) and SC O(1) solution for array related problem is two pointers.
### TC: O(n) and SC: O(1)
class Solution:
    def reOrderArrayTwo(self, array):
        lp = 0
        rp = len(array) - 1
        while lp < rp:
            while array[lp] % 2 != 0 and lp < rp:
                lp += 1
            while array[rp] % 2 == 0 and lp < rp:
                rp -=1
            array[lp], array[rp] = array[rp], array[lp] ### swap
        return array