'''
JZ28 对称的二叉树

描述：
给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode 
# @return bool

class Solution:
    def isSymmetrical(self, pRoot):
        def mirror(r1, r2):
            if r1 and r2:
                if r1.val == r2.val:
                    return mirror(r1.left, r2.right) and mirror(r1.right, r2.left)
                else:
                    return False
            elif r1 or r2:
                return False
            else:
                return True
        return mirror(pRoot, pRoot)