'''
Leetcode 235. Lowest Common Ancestor of a Binary Search Tree

Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
where we allow a node to be a descendant of itself.”
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode
# @param p TreeNode
# @param q TreeNode
# @return TreeNode

### Iterative Solution
### TC: O(n) and SC: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            parent_val = node.val
            if node.val == p.val or node.val == q.val: ### the first time a node's val equals to p or q, it means that the LCA has been found
                return node
            elif node.val < p.val and node.val < q.val:   
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else: ### Trick: if p and q are not in the same side, then we find the LCA
                return node