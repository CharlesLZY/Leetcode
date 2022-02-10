'''
Leetcode 121. Best Time to Buy and Sell Stock

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

# @param prices List[int] 
# @return int

'''
Since we can only buy and sell once. To make the profit max, we need to buy at the lowest price and sell at the highest price.
'''

### TC: O(n) and SC: O(1)
class Solution:
    def maxProfit(self, prices):
        low = float("inf")
        MAX = 0
        for p in prices: ### new price can always substruct the previous low price
            low = min(p, low) ### will keep updating the current lowest price
            MAX = max(MAX, p - low) ### only the current price will substract the lowest price
        return MAX


### Reverse Version
### TC: O(n) and SC: O(1)
class Solution:
    def maxProfit(self, prices):
        high = float("-inf")
        MAX = 0
        for p in prices[::-1]:
            high = max(p, high) ### will keep updating the current highest price
            MAX = max(MAX, high - p) ### only the current price will be substracted the highest price
        return MAX