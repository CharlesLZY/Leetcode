'''
Leetcode 354. Russian Doll Envelopes

Description:
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of 
one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.
'''

# @param envelopes List[List[int]]
# @return int


'''
Sort + Longest Increasing Subsequence(LC300)
Sort by (w, -h), so that the heights of envelopes with the same width will not appear in the increasing subsequence
'''

### DP Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        DP_table = [1]*len(envelopes)

        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    DP_table[i] = max(DP_table[i], DP_table[j]+1)
        return max(DP_table)

### Stack Solution 
### TC: O(n^2) and SC: O(n) (TC can be optimized to O(nlogn))
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        stack = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            cur = envelopes[i][1]
            if cur > stack[-1]:
                stack.append(cur)
            else:
                for j in range(len(stack)): ### can be optimized to binary search to find the first larger number
                    if stack[j] >= cur: ### trick: >= can ensure there is no duplicated number in stack(strictly increasing)
                        stack[j] = cur
                        break
        return len(stack)








