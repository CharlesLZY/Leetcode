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
            l1 = contain(cur.left, p)
            r1 = contain(cur.right, p)
            l2 = contain(cur.left, q)
            r2 = contain(cur.right, q)
            if cur == p and (l2 or r2):
                return cur
            elif cur == q and (l1 or r1):
                return cur
            elif l2 and r1:
                return cur
            elif l1 and r2:
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
                ### trick: there are 3 situations of LCA
                mid = node == p or node == q
                left = containPQ(node.left)
                right = containPQ(node.right)
                if mid + left + right == 2:
                    self.ans = node
                return mid or left or right

        containPQ(root)
        return self.ans
'''
Another intuitive solution
Maintain a hash table {node: parent} to store parent nodes of all nodes
When we find p and q, track their ancestors and return the first common one
'''
### TC: O(n) and SC: O(n)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parents = {root: None}
        stack = [root]

        ### record all nodes' parents
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        p_ancestor = set()
        
        while p:
            p_ancestor.add(p)
            p = parents[p]

        while q not in p_ancestor:
            q = parents[q]
        return q ### the first common ancestor