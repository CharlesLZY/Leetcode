'''
Leetcode 426. Convert Binary Search Tree to Sorted Doubly Linked List

Description:
You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. 
For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, 
and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

'''

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root Node
# @return Node


### TC: O(n) and SC: O(1)
class Solution:
    prev = None
    def treeToDoublyList(self, root):
        def inorder(node):
            if node is None:
                return
            else:
                inorder(node.left)

                node.left = self.prev
                if self.prev:
                    self.prev.right = node
                self.prev = node 

                inorder(node.right)

        if root is None: ### corner case: empty tree
            return None 

        MIN = root ### the leftmost node is the head of the linked list
        while MIN.left:
            MIN = MIN.left 

        MAX = root ### the rightmost node is the tail of the linked list
        while MAX.right:
            MAX = MAX.right

        inorder(root)

        MIN.left = MAX
        MAX.right = MIN

        return MIN
