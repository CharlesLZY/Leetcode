'''
JZ7 重建二叉树 

描述：
给定节点数为 n 二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pre List[int] 
# @param vin List[int]
# @return TreeNode

### TC: O(n) (if finding the index of an element in vin costs O(1)) and SC: O(n)
class Solution:
    def reConstructBinaryTree(self, pre, vin):
        if len(pre) == 0:
            return None

        root = TreeNode(pre[0])

        loc = vin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:loc+1], vin[:loc])
        root.right = self.reConstructBinaryTree(pre[loc+1:], vin[loc+1:])

        return root

### Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def reConstructBinaryTree(self, vin, post):
        if len(post) == 0:
            return None

        root = TreeNode(post[-1])

        loc = vin.index(post[-1])
        root.left = self.reConstructBinaryTree(vin[:loc], post[:loc])
        root.right = self.reConstructBinaryTree(vin[loc+1:], post[loc: len(post)-1])

        return root

### Leetcode 889. Construct Binary Tree from Preorder and Postorder Traversal
'''
Preorder and postorder can only clarift the parent-child relationship, but they can not specify the left and right sub-tree.
It is not possible to reconstruct a binary tree.
'''
class Solution:
    def constructFromPrePost(self, pre, post):
        if len(pre) == 0:
            return None

        root = TreeNode(pre[0])


        if len(pre) > 1:
            left_child = pre[1] ### suppose it is left child
            loc = post.index(left_child)
            root.left = self.constructFromPrePost(pre[1:loc+2], post[:loc+1])
            root.right = self.constructFromPrePost(pre[loc+2:], post[loc+1: len(post)-1])

        return root

'''
pre-order: 
[ root | left-child . . . | right-child . . . ]
          <- left tree ->    <- right tree -> 

post-order: 
[ . . . left-child | . . . right-child | root]
  <- left tree ->    <- right tree -> 

in-order
[ . left-child . . | root | . . right-child . ]
  <- left tree ->            <- right tree -> 
'''