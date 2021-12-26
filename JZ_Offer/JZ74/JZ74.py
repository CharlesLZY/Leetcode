'''
JZ74 和为S的连续正数序列

描述：
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列?
'''

# @param s int 
# @return List[List[int]]

### Two Pointer Solution
### TC: O(n) and SC: O(1)
class Solution:
    def FindContinuousSequence(self, s):
        ans = []
        def seq_sum(i,j):
            return (i+j)*(j-i+1)/2
        lp = 1 ### lp <= rp
        rp = 1
        while lp <= s//2:
            if seq_sum(lp,rp) == s:
                ans.append([i for i in range(lp, rp+1)])
                lp += 1
            elif seq_sum(lp,rp) < s:
                rp += 1
            else:
                lp += 1
        return ans