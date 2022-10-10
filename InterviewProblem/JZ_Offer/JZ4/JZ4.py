'''
JZ4 二维数组中的查找

描述：
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。
给定 target = 3，返回 false。
'''

# @param target int 
# @param array List[List[int]]
# @return bool

'''
Searching all kinds of sorted arrays should be implemented with binary search.
The key to this problem is to find the pivot (which we can help us know which side to go.
Arr 0  1  2  3  4
0   <  <  <  < pivot
1               >
2               >
3     tar       >
4               >

We can eliminate one row or column at a time.
'''

### TC: O(n+m) and SC: O(1)
class Solution:
    def Find(self, target, array):
        h, w = len(array), len(array[0])
        i, j = 0, w-1
        while i < h and j >= 0: ### start at right-upper corner of the array
            pivot = array[i][j]
            if pivot == target:
                return True
            elif pivot < target: ### go down
                i += 1
            else: # pivot > target ### go left
                j -= 1
        return False
        