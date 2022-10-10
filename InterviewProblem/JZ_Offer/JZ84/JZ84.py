'''
JZ 84 二叉树中和为某一值的路径(三)

描述：
给定一个二叉树root和一个整数值 sum ，求该树有多少路径的的节点值之和等于 sum 。
该题路径定义不需要从根节点开始，也不需要在叶子节点结束，但是一定是从父亲节点往下到孩子节点
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode
# @param target int
# @return int

class Solution:
    res = 0
    def FindPath(self, root, target):
        self.res = 0
        def DFS(node, target):
            if node is None:
                return 
            else:
                target -= node.val
                if target == 0:
                    self.res += 1
                DFS(node.left, target) ### the former path still counts
                DFS(node.right, target) ### the former path still counts

        if root: 
            DFS(root, target)
            self.FindPath(root.left, target) ### path is not required to start from root
            self.FindPath(root.right, target) ### path is not required to start from root

        return self.res
