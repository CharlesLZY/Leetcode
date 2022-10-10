'''
Leetcode 230. Kth Smallest Element in a BST

Description:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @param k int
# @return int

### TC: O(k) and SC: O(k)
class Solution:
    def kthSmallest(self, root, k):
    	if root:
            n = 0
            stack = [root]
            nextToVisit = root
            ans = []
            while stack:
                while nextToVisit.left:
                    
                    stack.append(nextToVisit.left)
                    nextToVisit = nextToVisit.left
                    

                cur = stack.pop()
                ans.append(cur.val)
                n += 1
                if n == k:
                    return cur.val

                if cur.right:
                    stack.append(cur.right)
                    nextToVisit = cur.right
        return -1