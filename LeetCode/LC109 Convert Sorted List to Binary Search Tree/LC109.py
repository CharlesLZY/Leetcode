'''
Leetcode 109. Convert Sorted List to Binary Search Tree

Description:
Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# @param head ListNode
# @return TreeNode

### TC: O(n) and SC: O(n)
class Solution:
    def sortedListToBST(self, head):
        def findMid(head):
            prev = None
            slow = head
            fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            return prev, slow
        
        def build(head):
            if head is None:
                return None
            elif head.next is None:
                return TreeNode(head.val)
            else:
                prev, mid = findMid(head)
                prev.next = None
                root = TreeNode(mid.val)
                root.left = build(head)
                root.right = build(mid.next)
                return root
            
        return build(head)
        
        