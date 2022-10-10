'''
Leetcode 101. Symmetric Tree

Description:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @return bool

'''
要比得两棵树放一起比，不能自己和自己比。
'''

### TC: O(n) and SC: O(n)
class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            elif t1 is None or t2 is None:
                return False
            else:
                if t1.val == t2.val:
                    return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left) ### punchline
                else:
                    return False
        return isMirror(root, root)
