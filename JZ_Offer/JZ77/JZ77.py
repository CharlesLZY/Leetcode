'''
JZ77 按之字形顺序打印二叉树

描述：
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRoot TreeNode 
# @return List[List[int]]

### BFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def Print(self, pRoot):
        if pRoot is None: ### corner case: empty tree
            return 
        ans = []
        queue = [(pRoot, 1)] ### BFS
        while queue:
            node, depth = queue.pop(0)
            if len(ans) < depth: ### enter a new level
                ans.append([])
            ans[depth-1].append(node.val)
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        for i in range(1, len(ans), 2): ### reverse for even number level
            ans[i].reverse()
        return ans
