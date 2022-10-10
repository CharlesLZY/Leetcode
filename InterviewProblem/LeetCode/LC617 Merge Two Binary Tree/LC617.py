'''
Leetcode 617. Merge Two Binary Trees

Description:
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. 
You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root1 TreeNode
# @param root2 TreeNode
# @return TreeNode

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def mergeTrees(self, root1, root2):
        def DFS(node, node1, node2):
            if node1 is None and node2 is None:
                return
            node.val = (node1.val if node1 else 0) + (node2.val if node2 else 0)
            if (node1 and node1.left) or (node2 and node2.left):
                node.left = TreeNode()
                DFS(node.left, node1.left if node1 else None, node2.left if node2 else None)
            if (node1 and node1.right) or (node2 and node2.right):
                node.right = TreeNode()
                DFS(node.right, node1.right if node1 else None, node2.right if node2 else None)
        if root1 or root2:
            root = TreeNode()
            DFS(root, root1, root2)
            return root


### Better Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def mergeTrees(self, root1, root2):
        if root1 is None: ### use root1 to achieve inplace
            return root2 

        stack = [(root1, root2)]
        while stack:
            node1, node2 = stack.pop() ### node1 must not be None
            if node2 is None: ### trick: if node1 or node2 is None, the node should be handle correctly before this recursion
                continue
            node1.val += node2.val
            if node1.left is None: ### we don't check node2 because if node2 has no child, node1 does not need to be updated
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))

            if node1.right is None: ### we don't check node2 because if node2 has no child, node1 does not need to be updated
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))

        return root1


