'''
JZ36 二叉搜索树与双向链表

描述：
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param pRootOfTree TreeNode
# @return TreeNode

'''
The inorder traversal sequence of a binary search tree is sorted.
So what we need to do is to inorder traverse the binary search tree and link the node with its predecessor
'''
### TC: O(n) and SC: O(1)
class Solution:
    prev = None
    def Convert(self, pRootOfTree):

        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)
                node.left = self.prev ### handle the link
                if self.prev:
                    self.prev.right = node ### handle the link
                self.prev = node ### update prev
                inorder(node.right)


        if pRootOfTree is None: ### corner case: empty tree
            return None

        MIN = pRootOfTree ### the leftmost node is the head of the linked list
        while MIN.left:
            MIN = MIN.left

        inorder(pRootOfTree)

        return MIN



