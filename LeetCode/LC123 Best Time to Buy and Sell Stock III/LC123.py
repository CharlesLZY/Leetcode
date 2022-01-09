'''
Leetcode 123. Best Time to Buy and Sell Stock III

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''

# @param prices List[int] 
# @return int


'''
Divide this problem in to two sub-problem just like LC121. 
Since LC121 can be solved in two directions (tracking the lowest or highest price),
we can pick up the division between two transactions and solve two sub-problems
'''

### DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def maxProfit(self, prices):
        MAX = 0
        leftMin = prices[0]
        leftProfits = [0] * len(prices) ### DP = 
        for lp in range(1, len(prices)): 
            leftProfits[lp] = max(leftProfits[lp-1], prices[lp] - leftMin)
            leftMin = min(leftMin, prices[lp])

        rightMax = prices[-1]
        rightProfits = [0] * len(prices)
        for rp in range(len(prices)-2, -1, -1):  ### rp go through the prices in reverse 
            rightProfits[rp] = max(rightProfits[rp+1], rightMax - prices[rp])
            rightMax = max(rightMax, prices[rp])

        ### if sell the stock then buy it immediately then sell it again, then this is equal to hold it and then sell it
        for i in range(len(prices)):
            MAX = max(MAX, leftProfits[i] + rightProfits[i])
        return MAX




