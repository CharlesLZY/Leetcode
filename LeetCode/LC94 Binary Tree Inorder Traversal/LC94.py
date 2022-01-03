'''
Leetcode 94. Binary Tree Inorder Traversal

Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return List[int]

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def inorderTraversal(self, root):
        ans = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def inorderTraversal(self, root):
        if root is None: ### corner case
            return []
        ans = []
        stack = [root]
        while stack:
            if stack[-1]: ### keep push left branch to stack
                stack.append(stack[-1].left) ### ensure that left branch must be visited before node itself
            else: ### use None to determine whether the node can be visited
                '''
                       parent
                      /
                   child
                   /  \
                None  None
                
                left None -> visit the leaf node
                after the node is visited, push its right child into the stack
                right(most) None (which means left child finished) -> visit parent
                '''
                stack.pop() ### pop the None
                if stack:
                    node = stack.pop()
                    ans.append(node.val)
                    stack.append(node.right)
        return ans
