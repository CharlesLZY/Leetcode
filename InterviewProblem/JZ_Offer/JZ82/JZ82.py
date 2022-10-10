'''
JZ82 二叉树中和为某一值的路径(一)

描述：
给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode 
# @param sum int
# @return bool

'''
This problem is simple, because the path must start from root and end at the left node (with no child).
'''

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def hasPathSum(self, root, S):
        def add(node, res):
            res = res + node.val
            if node.left is None and node.right is None: ### leaf node
                if res == S:
                    return True
                else:
                    return False
            else:
                return (add(node.left, res) if node.left else False) or (add(node.right, res) if node.right else False)
        if root is None: ### corner case: empty tree
            return False
        else:
            return add(root, 0)


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def hasPathSum(self, root, S):
        if root is None: ### corner case: empty tree
            return False
        stack = [(root, 0)]
        while stack:
            cur, res = stack.pop()
            res = res + cur.val
            if cur.left is None and cur.right is None: ### leaf node
                if res == S:
                    return True
                else:
                    continue ### different from Recursive Solution, no need to return False, just move forward
            else:
                if cur.left:
                    stack.append((cur.left, res))
                if cur.right:
                    stack.append((cur.right, res))
        return False


