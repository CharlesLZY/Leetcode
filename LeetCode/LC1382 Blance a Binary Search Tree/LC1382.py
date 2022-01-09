'''
Leetcode 1382. Balance a Binary Search Tree

Description:
Given the root of a binary search tree, return a balanced binary search tree with the same node values. 
If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @return TreeNode

### TC: O(n) and SC: O(n)
class Solution:
    def balanceBST(self, root):
        array = []
        def inorder(node): ### inorder of BST is a sorted array
            if node:
                inorder(node.left)
                array.append(node.val)
                inorder(node.right)


        def build(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])

            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            return root

        inorder(root) ### convert this problem into LC108: convert a sorted array to a balanced BST

        return build(array)