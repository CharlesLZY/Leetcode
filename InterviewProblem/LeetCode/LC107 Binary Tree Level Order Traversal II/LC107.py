'''
Leetcode 107. Binary Tree Level Order Traversal II

Description:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).
'''

# @param root TreeNode
# @return List[List[int]]

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### TC: O(n) and SC: O(n)
class Solution:
    def levelOrderBottom(self, root):
        ans = []
        if root:
            queue = [(root,0)]
            while queue:
                node, depth = queue.pop(0)
                if len(ans) <= depth:
                    ans.append([])
                ans[depth].append(node.val)
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
        ans.reverse()
        return ans