'''
JZ85 连续子数组的最大和(二)

描述：
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，找到一个具有最大和的连续子数组。
1.子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组
2.如果存在多个最大和的连续子数组，那么返回其中长度最长的，该题数据保证这个最长的只存在一个
3.该题定义的子数组的最小长度为1，不存在为空的子数组，即不存在[]是某个数组的子数组
4.返回的数组不计入空间复杂度计算
'''

# @param array List[int] 
# @return List[int]

### TC: O(n) and SC: O(1)
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        MAX = array[0]
        cur = array[0]  
        lp = 0
        rp = 1
        cur_lp = 0
        cur_rp = 1

        for i in range(1, len(array)):
            ### if array[i]  + cur < array[i]: ### refer to JZ42
            if array[i]  + cur < 0 or cur < 0:
                cur_lp = i
                cur_rp = i+1
            else:
                cur_rp += 1
            cur = max(array[i], cur+array[i])
            if cur > MAX:
                lp = cur_lp
                rp = cur_rp
                MAX = cur
            elif cur == MAX:
                if rp - lp < cur_rp - cur_lp: ### keep the longer sub-sequence
                    lp = cur_lp
                    rp = cur_rp

        return array[lp:rp]