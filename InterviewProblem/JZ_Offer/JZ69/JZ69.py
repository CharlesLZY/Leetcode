'''
JZ69 跳台阶

描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

# @param number int
# @return int

### DP Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        DP_table = [0]*number ### DP[i] denotes the number of ways to reach on ith step
        DP_table[0] = 1 
        DP_table[1] = 2
        for i in range(2, number):
            DP_table[i] = DP_table[i-1] + DP_table[i-2]
        return DP_table[number-1]


### DP Space Complexity Optimized Solution
### TC: O(n) and SC: O(1)
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        prev = 1
        cur = 2
        for i in range(2, number):
            cur, prev = cur+prev, cur
        return cur