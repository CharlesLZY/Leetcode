'''
Leetcode 322. Coin Change

Description:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

# @param coins List[int] 
# @param amount int 
# @return int


### Brute Solution
### TC O(S^n) and SC: O(S^n)  where S is the amount, n is denomination count
class Solution:
    MIN = float("inf")
    def coinChange(self, coins, amount):
        self.MIN = float("inf")
        def DFS(path, res):
            if res < 0:
                return 
            if res == 0:
                self.MIN = min(self.MIN, len(path))
                return 
            for c in coins:
                path.append(c)
                DFS(path, res-c)
                path.pop()
        DFS([], amount)
        if self.MIN == float("inf"): ### corner case
            return -1
        return self.MIN


'''
DP[S] = min DP[S - c] + 1 where DP[S] is the min number of coins to make change for S
         c
'''
### DP Solution
### TC: O(S*n) and SC: O(S) where S is the amount, n is denomination count
class Solution:
    def coinChange(self, coins, amount):
        DP_table = [float("inf")] * (amount+1)
        DP_table[0] = 0
        for i in range(min(coins), amount + 1):
            candidates = []
            for c in coins:
                if i - c < 0:
                    continue
                else:
                    candidates.append(DP_table[i-c])
            DP_table[i] = min(candidates) + 1
        return DP_table[-1] if DP_table[amount] != float("inf") else -1


### Greedy Solution (类似LC279, 先把上界划出来，然后一个一个试，期望上能减小运算量)
class Solution:
    def coinChange(self, coins, amount):
        def DFS(res, count):
            if count == 0:
                if res != 0:
                    return False
                else:
                    return True
            else:
                for c in coins:
                    if c > res:
                        break
                    else:
                        if DFS(res-c, count-1):
                            return True
                return False
        lb = amount // max(coins) ### 最少这么多张
        hb = amount // min(coins) + 1 ### 最多这么多张
        for i in range(lb, hb):
            if DFS(amount, i):
                return i
        return -1
