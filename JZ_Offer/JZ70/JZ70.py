'''
JZ70 矩形覆盖

描述：
我们可以用 2*1 的小矩形横着或者竖着去覆盖更大的矩形。请问用 n 个 2*1 的小矩形无重叠地覆盖一个 2*n 的大矩形，从同一个方向看总共有多少种不同的方法？
'''

# @param number int 
# @return int


'''
Similar to climbing stairs problem
'''
### TC O(n) and SC: O(1)
class Solution:
    def rectCover(self, number):
        if number == 0: ### corner case
            return 0
        prev = 1
        cur = 1
        for i in range(1, number):
            cur, prev = prev+cur, cur
        return cur