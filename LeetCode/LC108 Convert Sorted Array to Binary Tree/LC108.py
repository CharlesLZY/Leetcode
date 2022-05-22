'''
Leetcode 108. Convert Sorted Array to Binary Search Tree

Description:
Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which 
the depth of the two subtrees of every node never differs by more than one.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param nums List[int]
# @return TreeNode

'''
这题要求height-balanced
'''

### TC: O(n) and SC: O(n)
class Solution:
    def sortedArrayToBST(self, nums):
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

        return build(nums)




        