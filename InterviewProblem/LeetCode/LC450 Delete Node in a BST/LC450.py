'''
Leetcode 450. Delete Node in a BST

Description:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
- Search for a node to remove.
- If the node is found, delete the node.

Constraint: Each node has a unique value.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @param key int
# @return TreeNode

### TC: O(H) and SC: O(H)
class Solution:
    def deleteNode(self, root, key): ### trick: always return a node
        def successor(node): ### leftmost right child
            if node:
                node = node.right
                while node.left:
                    node = node.left
                return node
            else: ### will never enter
                return None

        def predecessor(node): ### rightmost left child
            if node:
                node = node.left
                while node.right:
                    node = node.right
                return node
            else: ### will never enter
                return None


        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: ### delete current node
            if root.right:
                root.val = successor(root).val
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                root.val = predecessor(root).val
                root.left = self.deleteNode(root.left, root.val)
            else: ### trick: if leaf node, delete itself by returning None, which will update its parent's child
                return None ### the recursive call is like node.left/right = deleteNode(), so return None is exactly what we want

        return root