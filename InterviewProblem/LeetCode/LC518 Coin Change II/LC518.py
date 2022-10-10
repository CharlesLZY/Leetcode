'''
Leetcode 518. Coin Change 2

Description:
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.
'''

# @param amount int
# @param coins List[int] 
# @return int

'''

'''
### DP Solution
### TC: O(S*n) and SC: O(S) where S is the amount, n is denomination count
class Solution:
    def change(self, amount, coins):
        DP_Table = [0] * (amount + 1)
        DP_Table[0] = 1

        for c in coins: ### only use one type of coin
            for n in range(c, amount + 1): ### when we currently make up n dollars, we then add c dollors
                DP_Table[n] += DP_Table[n - c] ### if the last coin is c, how many ways to make up n dollors
        return DP_Table[-1]
