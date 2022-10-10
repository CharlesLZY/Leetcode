'''
Leetcode 122. Best Time to Buy and Sell Stock II

Description:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

# @param prices List[int] 
# @return int

'''
Difference from LC121, we can buy and sell for any times. So we can take the greedy strategy: make money when there is any profit
'''

### TC: O(n) and SC: O(1)
class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)): 
            if prices[i] > prices[i-1]: ### greedy strategy
                res += prices[i] - prices[i-1]
        return res