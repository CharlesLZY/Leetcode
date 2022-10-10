'''
JZ14 剪绳子

描述：

给你一根长度为 n 的绳子，请把绳子剪成整数长的 m 段（ m 、 n 都是整数， n > 1 并且 m > 1 ， m <= n ），
每段绳子的长度记为 k[1],...,k[m] 。请问 k[1]*k[2]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18 。
'''

# @param number int
# @return int

### TC: O(n^2) and SC: O(n)
class Solution:
    DP_table = [0] * 60
    def cutRope(self, number): ###  return DP[n], if DP[n] is empty, it will update DP[n]
        if number <= 2:
            return 1
        if self.DP_table[number] > 0: ### DP[n] has been calculated
            return self.DP_table[number]
        else:
            MAX = 0
            for i in range(1, number): ### how long can one cut be (1 <= cut < number)
                MAX = max(MAX, i * max(self.cutRope(number-i), number-i)) ### trick: i * max(self.cutRope(number-i), number-i)
                ### cutRope(n) will return DP[n], if DP[n] is empty, it will calculate DP[n]
                ### DP[n] at least cut one time, so we need i * max(cutRope(number-i), number-i). number - i means no cut
            self.DP_table[number] = MAX
            return MAX

