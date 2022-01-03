'''
JZ34 二叉树中和为某一值的路径(二)

描述：
输入一颗二叉树的根节点root和一个整数expectNumber，找出二叉树中结点值的和为expectNumber的所有路径。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode 
# @param target int 
# @return List[List[int]]

'''
This problem is simple, because the path must start from root and end at the left node (with no child).
'''

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    ans = []
    def FindPath(self, root, target):
        def add(node, res, path):
            res += node.val
            path.append(node.val)
            if node.left is None and node.right is None: ### leaf node
                if res == target:
                    self.ans.append(path[:])
            else:
                if node.left:
                    add(node.left, res, path)
                if node.right:
                    add(node.right, res, path)
            path.pop() ### backtrack

        if root: ### corner case: empty tree
            add(root, target, [])
        return self.ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    ans = []
    def FindPath(self, root, target):
        if root:
            stack = [(root, 0, [])] ### the path has to be stored
            while stack:
                node, res, path = stack.pop()
                path.append(node.val)
                res = res + node.val
                if node.left is None and node.right is None: ### leaf node
                    if res == target:
                        self.ans.append(path[:])
                else:
                    if node.left:
                        stack.append((node.left, res, path[:]))
                    if node.right:
                        stack.append((node.right, res, path[:]))
        return self.ans
