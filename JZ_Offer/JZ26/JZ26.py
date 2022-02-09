'''
JZ26 树的子结构

描述：
输入两棵二叉树A，B，判断B是不是A的子结构。（我们约定空树不是任意一个树的子结构）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot1 TreeNode
# @param pRoot2 TreeNode
# @return bool

### TC: O(mn) and SC: O(n)
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        def isSame(p1, p2):
            if p1: ### p2 must not be None
                if p1.val == p2.val:
                    left = isSame(p1.left, p2.left) if p2.left else True
                    right = isSame(p1.right, p2.right) if p2.right else True
                    return left and right

                else: 
                    return False
            else: ### p2 must not be None, so if p1 is None, return False
                return False

        if pRoot2 is None: ### corner case: empty tree is not considered as a sub-tree
            return False

        if pRoot1:
            res = False
            if pRoot1.val == pRoot2.val:
                res = isSame(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
            return res
        else:
            return False