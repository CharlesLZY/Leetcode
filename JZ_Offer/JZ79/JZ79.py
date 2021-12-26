'''
JZ79 判断是不是平衡二叉树

描述：
输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：
它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode
# @return bool

### Easy to understand
class Solution:
    def IsBalanced_Solution(self, pRoot):
        def depth(node):
            if node:
                return max(depth(node.left), depth(node.right)) + 1
            else:
                return 0

        if pRoot is None:
            return True

        if abs(depth(pRoot.left) - depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

### TC: O(n) and SC: O(n)
class Solution:
    def IsBalanced_Solution(self, pRoot):
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            if left == -1 or right == -1:
                return -1 ### not balance
            else:
                if abs(left - right) > 1:
                    return -1 ### not balance
                else:
                    return max(left, right) + 1

        return depth(pRoot) != -1
