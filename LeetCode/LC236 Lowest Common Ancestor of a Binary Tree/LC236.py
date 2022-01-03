'''
Leetcode 236. Lowest Common Ancestor of a Binary Tree

Description:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode 
# @param p TreeNode
# @param q TreeNode
# @return TreeNode

'''
3 situations of LCA (Lowest Common Ancestor)
1. 
      [p]
     /   \
   ...   ...
           \
           [q]

2. 
      [p]
     /   \
   ...   ...
   /    
 [q]

3. 
      [ ]
     /   \
   ...   ...
   /       \
 [p]       [q]

'''

### Easy to understand solution (A lot to optimize)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def contain(node, target): ### whether the sub-tree whose root is node contains the target
            if node is None:
                return False
            elif node == target:
                return True
            else:
                return contain(node.left, target) or contain(node.right, target)

        queue = [root] ### BFS
        while queue:
            cur = queue.pop(0)
            if cur == p and (contain(cur.left, q) or contain(cur.right, q)):
                return cur
            elif cur == q and (contain(cur.left, p) or contain(cur.right, p)):
                return cur
            elif contain(cur.left, q) and contain(cur.right, p):
                return cur
            elif contain(cur.left, p) and contain(cur.right, q):
                return cur
            else:
                if cur.left: 
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

### TC: O(n) and SC: O(n)
class Solution:
    ans = None
    def lowestCommonAncestor(self, root, p, q):
        def containPQ(node):
            if node is None:
                return False
            else:
                mid = node == p or node == q
                left = contain(node.left)
                right = contain(node.right)
                if mid + left + right == 2:
                    self.ans = node
                return mid or left or right

        containPQ(root)
        return self.ans
