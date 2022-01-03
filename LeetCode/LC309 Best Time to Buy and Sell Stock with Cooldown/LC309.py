'''
Leetcode 309. Best Time to Buy and Sell Stock with Cooldown

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

# @param prices List[int] 
# @return int

### TC: O(n) and SC: O(1)
class Solution():
    def maxProfit(self, prices):
        '''

     _____                      _____
    |     |                    |     |
    ---> hold  ->  sold  ->  ready<---
          ^                    |
          |____________________|

        sold[i]  = hold[i−1] + price[i]
        hold[i]  = max(hold[i−1], ready[i−1] − price[i])
        ready[i] = max(ready[i−1], sold[i−1])


        '''
        ### DP table of sold, hold and ready states
        sold_DP = [None]*(len(prices)+1)
        hold_DP = [None]*(len(prices)+1)
        ready_DP = [None]*(len(prices)+1)

        sold_DP[0] = float("-inf") ### inexisted
        hold_DP[0] = float("-inf") ### inexisted
        ready_DP[0] = 0

        for i in range(len(prices)):
            sold_DP[i+1] = hold_DP[i] + prices[i]
            hold_DP[i+1] = max(hold_DP[i], ready_DP[i]-prices[i])
            ready_DP[i+1] = max(ready_DP[i], sold_DP[i])

        return max(sold_DP[len(prices)], ready_DP[len(prices)])