'''
JZ27 二叉树的镜像

描述：
操作给定的二叉树，将其变换为原二叉树的镜像。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode 
# @return TreeNode

### TC: O(n) and SC: O(n)
class Solution:
    def Mirror(self, pRoot):
        if pRoot:
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
            self.Mirror(pRoot.left)
            self.Mirror(pRoot.right)

        return pRoot