'''
JZ78 把二叉树打印成多行

描述：
给定一个节点数为 n 二叉树，要求从上到下按层打印二叉树的 val 值，同一层结点从左至右输出，
每一层输出一行，将输出的结果存放到一个二维数组中返回。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode
# @return List[List[int]]

### TC: O(n) and SC: O(n)
class Solution:
    def Print(self, pRoot):
        ans = []
        queue = [(pRoot, 1)] ### BFS
        while queue:
            node, depth = queue.pop(0)
            if node:
                if len(ans) < depth:
                    ans.append([])
                ans[depth-1].append(node.val)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))
        return ans