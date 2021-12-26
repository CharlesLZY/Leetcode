'''
JZ57 和为S的两个数字

描述：
输入一个递增排序的数组array和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，返回任意一组即可，如果无法找出这样的数字，返回一个空数组即可。
'''

# @param array List[int] 
# @param s int
# @return List[int]

### TC: O(n) and SC: O(1)
class Solution:
    def FindNumbersWithSum(self, array, s):
        ### since the array is sorted, we can use two pointers
        lp = 0
        rp = len(array) - 1
        ans = []
        while lp < rp:
            if array[lp] + array[rp] > s:
                rp -= 1
            elif array[lp] + array[rp] < s:
                lp += 1
            else:
                ans = [array[lp], array[rp]]
                break
        return ans