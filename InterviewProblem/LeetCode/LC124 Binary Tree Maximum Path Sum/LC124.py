'''
Leetcode 124. Binary Tree Maximum Path Sum

Description:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return int

'''
Similar to LC543
The difficult part of this problem is that the path can start from child. e.g. left -> root -> right
'''

### TC: O(n) and SC: O(n)
class Solution:
    def maxPathSum(self, root):
        self.MAX = float("-inf")
        def maxHalfPath(node): ### the max path sum of all paths end at the node, node.val + max(leftPath, rightPath)
            if node is None:
                return 0
            leftPath = max(maxHalfPath(node.left), 0) ### maxHalfPath(node) must contain the node
            rightPath = max(maxHalfPath(node.right), 0) ### trick: we can choose to abandon the child branch if it is negative, so we use max( _ , 0) 
            ### each node will only be iterated once, so we need to check the case that the node is at the middle of the whole path (left -> root -> right)
            self.MAX = max(self.MAX, leftPath + node.val + rightPath) ### path sum when the node is at middle >= path sum when node is at end 
            return node.val + max(leftPath, rightPath)
        
        maxHalfPath(root)
        
        return self.MAX


