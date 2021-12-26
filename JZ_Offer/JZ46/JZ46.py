'''
JZ46 把数字翻译成字符串

描述：
有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。
现在给一串数字，返回有多少种可能的译码结果
'''

'''
牛客网这题傻逼，册那0都没对应字母
'''

# @param nums str
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def solve(self, nums):
        if nums[0] == '0': ### corner case
            return 0
        DP_table = [0] * (len(nums)+1) ### DP table can be optimize to O(1) space complexity by only store DP[i-1] and DP[i-2]
        DP_table[0], DP_table[1] = 1, 1 ### DP[i] represents until the ith bit, how many kinds of representations
        for i in range(1,len(nums)):
            if nums[i-1:i+1] == "00": ### so stupid, without considering 0
                return 0

            if "11" <= nums[i-1:i+1] and nums[i-1:i+1] <= "26" and nums[i-1:i+1] != "20": ### so stupid, no letter corresponds to 0, so 20 can only be represented by t
                DP_table[i+1] = DP_table[i] + DP_table[i-1] 
            else:
                DP_table[i+1] = DP_table[i]
        return DP_table[len(nums)]

'''
力扣版本：
字母编码方式改成：'a'->0, 'b->1', ... , 'z->25'。
'''

# @param num int
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def translateNum(self, num):
        prev_1 = 1
        prev_2 = 1
        for i in range(1, len(str(num))):
            temp = num % 100
            if 10 <= temp and temp <= 25:
                prev_1, prev_2 = prev_2, prev1+prev_2
            else:
                prev_1 = prev_2
            num = num // 10
        return prev_2