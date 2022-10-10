'''
Leetcode 103. Binary Tree Zigzag Level Order Traversal

Description:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return List[List[int]]

### DFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        else:
            res = []
            def DFS(node, depth):
                if depth >= len(res):
                    res.append([node.val])
                else:
                    if depth % 2 == 1:
                        res[depth].insert(0, node.val)
                    else:
                        res[depth].append(node.val)

                if node.left:
                    DFS(node.left, depth+1)
                if node.right:
                    DFS(node.right, depth+1)

            DFS(root, 0)
            return res
