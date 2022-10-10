'''
Leetcode 114. Flatten Binary Tree to Linked List

Description:
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points 
to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return None

### Intuitive Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def flatten(self, root):
        def straighten(node):
            if node is None:
                return None
            ### IMPORTANT BASE CASE
            if node.left is None and node.right is None: ### trick
                return node
            leftTail = straighten(node.left) ### recursivly flatten sub-tree, get the rightmost node of the flatten sub-tree
            rightTail = straighten(node.right) ###  the rightmost node of the flatten right sub-tree will be the rightmost node for the current flatten tree
            if node.left:
                leftTail.right = node.right ###     root                 root
                node.right = node.left      ###    /    \      ---->         \
                node.left = None            ###  left  right                 left
                                            ###                                \
                                            ###                                right
            return  rightTail if rightTail else leftTail ### return the rightmost node
        straighten(root)

### Iterative Solution
### TC: O(n) and SC: O(1)
class Solution:
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                if cur.right:
                    left_rightmost = cur.left
                    while left_rightmost.right:
                        left_rightmost = left_rightmost.right
                    left_rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right


#               1                   1                    1                     1
#             /   \                  \                    \                     \ 
#            2     3       ->         2         ->         2         ->          2
#           / \   / \                / \                    \                     \
#          4   5 6   7              4   5                    4                     4
#                                        \                    \                     \
#                                         3                    5                     5
#                                        / \                    \                     \
#                                       6   7                    3                     3
#                                                               / \                     \
#                                                              6   7                     6
#                                                                                         \
#                                                                                          7