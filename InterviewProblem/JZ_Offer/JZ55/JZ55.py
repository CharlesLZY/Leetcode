'''
JZ55 二叉树的深度

描述：
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度，根节点的深度视为 1 。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
        else:
            return 0

class Solution:
    res = 0
    def TreeDepth(self, pRoot):
        self.res = 0
        def DFS(node, depth):
            if node:
                self.res = max(self.res, depth + 1)
                DFS(node.left, depth + 1)
                DFS(node.right, depth + 1)
        DFS(pRoot, 0)
        return self.res

class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None: ### corner case: empty tree
            return 0
        
        stack = [(pRoot, 1)]
        MAX_depth = float("-inf")
        while stack:
            node, depth = stack.pop()
            if node.left or node.right:
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))
            else:
                MAX_depth = max(MAX_depth, depth)
        return MAX_depth
