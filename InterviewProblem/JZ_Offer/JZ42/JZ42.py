'''
JZ42 连续子数组的最大和

描述：
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
'''

# @param array List[int]
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        MAX = array[0]
        cur = array[0]

        for n in array[1:]:
            cur = max(n, cur+n)
            MAX = max(cur, MAX)
        return MAX

'''
Intuitive DP Solution
DP[i] Maximum sum of sub-array ending at i ### the key point: sub-array ending at i
State transition equation: DP[i] = max(DP[i-1]+array[i], array[i])
'''
### TC: O(n) and SC: O(n)
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        DP_table = [0]*len(array)
        DP_table[0] = array[0]
        for i in range(1, len(array)):
            DP_table[i] = max(array[i], DP_table[i-1] + array[i])
        return max(DP_table)