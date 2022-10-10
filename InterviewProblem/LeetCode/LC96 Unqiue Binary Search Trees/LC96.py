'''
Leetcode 96. Unique Binary Search Trees

Description:
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

# @param num int 
# @return int

'''
BST is a recursive structure. For a sorted list of numbers, as long as we selected the root, 
1 2 3 ... r-1 | r | r+1 ... n-1 n
1:r-1 will be the left branch, r+1:n will be the right branch
The branch of BST is also a BST.
DP[n] = F(1,n) + F(2,n) + ... + F(n,n)
F(i,n) is the number of BST structures when the root is set as i
F(i,n) = G(i-1)*G(n-i)
'''
### DP Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def numTrees(self, num):
        DP_table = [0]*(num+1)
        DP_table[0] = 1 ### trick: empty tree counts for one structure
        DP_table[1] = 1 
        for n in range(2, num+1): ### iterate different root DP[i]
            for i in range(1, n+1): ### F(i,n)
                DP_table[n] += DP_table[i-1] * DP_table[n-i]
        return DP_table[num]