'''
JZ86 在二叉树中找到两个节点的最近公共祖先

描述：
给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。

注：本题保证二叉树中每个节点的val值均不相同
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode
# @param o1 int
# @param o2 int
# @return int

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
    def lowestCommonAncestor(self, root, o1, o2):
        def contain(node, target):
            if node is None:
                return False
            elif node.val == target:
                return True
            else:
                return contain(node.left, target) or contain(node.right, target)

        queue = [root] ### BFS
        while queue:
            cur = queue.pop(0)
            if cur.val == o2 and (contain(cur.left, o1) or contain(cur.right, o1)):
                return cur.val
            elif cur.val == o1 and (contain(cur.left, o2) or contain(cur.right, o2)):
                return cur.val
            elif contain(cur.left, o1) and contain(cur.right, o2):
                return cur.val
            elif contain(cur.left, o2) and contain(cur.right, o1):
                return cur.val
            else:
                if cur.left: 
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

class Solution:
    def lowestCommonAncestor(self, root, o1, o2):
        def contain(node, target):
            if node is None:
                return False
            elif node.val == target:
                return True
            else:
                return contain(node.left, target) or contain(node.right, target)

        queue = [root] ### BFS
        while queue:
            cur = queue.pop(0)
            l1 = contain(cur.left, o1)
            r1 = contain(cur.right, o1)
            l2 = contain(cur.left, o2)
            r2 = contain(cur.right, o2)
            if cur.val == o2 and (l1 or r1):
                return cur.val
            elif cur.val == o1 and (l2 or r2):
                return cur.val
            elif l1 and r2:
                return cur.val
            elif l2 and r1:
                return cur.val
            else:
                if cur.left: 
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)


### TC: O(n) and SC: O(n)
class Solution:
    ans = None
    def lowestCommonAncestor(self, root, o1, o2):
        def contain(node):
            if node is None:
                return False
            else:
                mid = node.val == o1 or node.val == o2
                left = contain(node.left)
                right = contain(node.right)
                if mid + left + right == 2:
                    self.ans = node.val
                return mid or left or right

        contain(root)
        return self.ans