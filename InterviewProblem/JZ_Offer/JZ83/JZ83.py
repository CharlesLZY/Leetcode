'''
JZ83 剪绳子(进阶版)

描述：
给你一根长度为 n 的绳子，请把绳子剪成整数长的 m 段（ m 、 n 都是整数， n > 1 并且 m > 1 ， m <= n ），
每段绳子的长度记为 k[1],...,k[m] 。请问 k[1]*k[2]*...*k[m] 可能的最大乘积是多少？
例如，当绳子的长度是 8 时，我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18 。

由于答案过大，请对 998244353 取模。
'''

# @param number int 
# @return int

'''
通过观察
4: 2x2
5: 2x3
6: 3x3
7: 2x3x3
8: 2x3x3
9: 3x3x3
...
能拆出3就拆，不能就拆2

((a mod n)(b mod n)) mod n = ab mod n

'''
#
class Solution:
    def cutRope(self, number):
        def fastPower(b, n):
            ans = 1
            while n:
                if n&1: ### last bit is 1
                    ans = ans* b % 998244353
                b = b * b % 998244353 ### base
                n >>= 1
            return ans

        if number == 1:
            return 1
        if number == 2:
            return 1
        if number == 3:
            return 2
        mod = number % 3
        if mod == 1: ### 2x2x3^k
            return 4*fastPower(3, (number - 4) // 3) % 998244353
        elif mod == 2: ### 2x3^k
            return 2*fastPower(3, (number - 2) // 3) % 998244353
        else:
            return fastPower(3, number // 3) % 998244353

### DP Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    DP_table = [0] * 60
    def cutRope(self, number):
        if number <= 2:
            return 1
        if self.DP_table[number] > 0:
            return self.DP_table[number]
        else:
            MAX = 0
            for i in range(1, number): ### how long can one cut be (1 <= cut < number)
                MAX = max(MAX, i * max(self.cutRope(number-i), number-i)) ### trick: i * max(self.cutRope(number-i), number-i)
                ### cutRope(n) will return DP[n], if DP[n] is empty, it will calculate DP[n]
                ### DP[n] at least cut one time, so we need max(cutRope(number-i), number-i). number - i means no cut
            self.DP_table[number] = MAX
            return MAX
