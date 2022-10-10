'''
JZ32 从上往下打印二叉树

描述：
不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode
# @return List[int]

### TC: O(n) and SC: O(n)
class Solution:
    def PrintFromTopToBottom(self , root):
        res = []
        queue = []

        if root is None: ### corner case
            return res

        queue.append(root)
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return res

