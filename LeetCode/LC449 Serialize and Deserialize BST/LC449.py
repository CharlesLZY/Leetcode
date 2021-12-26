'''
Leetcode 449. Serialize and Deserialize BST

Description:
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization 
algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized 
to the original tree structure.

The encoded string should be as compact as possible. 
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Comparing with normal binary tree, we can make the encoded string more compact with the property of BST
Binary Tree could be constructed from preorder/postorder and inorder traversal.
Inorder traversal of BST is an array sorted in the ascending order: inorder = sorted(preorder).
Therefore, once we get the inorder/postorder of BST, we can reconstruct it.
'''

class Codec:

    def serialize(self, root):
        def preorder(root):
            return [str(root.val)] + preorder(root.left) + preorder(root.right) if root else ['#'] 
        return ';'.join(preorder(root))

    def deserialize(self, data):
        def reconstruct(preorder, inorder):
            if preorder:
                root = TreeNode(preorder[0])
                idx = inorder.index(preorder[0])
                root.left = reconstruct(preorder[1:idx+1], inorder[:idx])
                root.right = reconstruct(preorder[idx+1:], inorder[idx+1:])
                return root
            else:
                return None

        preorder = [int(x) for x in data.split(';') if x != '#']
        inorder = preorder[:]
        inorder.sort()
        return reconstruct(preorder, inorder)