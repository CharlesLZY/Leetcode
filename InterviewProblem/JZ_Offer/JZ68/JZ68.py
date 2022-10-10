'''
JZ68 二叉搜索树的最近公共祖先

描述：
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
1.对于该题的最近的公共祖先定义:对于有根树T的两个结点p、q，最近公共祖先LCA(T,p,q)表示一个结点x，满足x是p和q的祖先且x的深度尽可能大。
在这里，一个节点也可以是它自己的祖先.
2.二叉搜索树是若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值
3.所有节点的值都是唯一的。
4.p、q 为不同节点且均存在于给定的二叉搜索树中。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param root TreeNode 
# @param p int 
# @param q int
# @return int

### General Solution to find LCA in binary tree
### TC: O(n) and SC: O(n)
class Solution:
    ans = None
    def lowestCommonAncestor(self, root, p, q):
        def contain(node):
            if node is None:
                return False
            mid = node.val == p or node.val == q
            left = contain(node.left)
            right = contain(node.right)
            if mid + left + right == 2:
                self.ans = node.val
            return mid or left or right
        contain(root)
        return self.ans


### Utilizing the property of BST, we can simplify the former solution. The problem assumes that all nodes have different values.
'''
Three situations of LCA in BST will be much easier to decide:
1. if p.val / q.val < node.val and q.val/p.val > node.val, the node is the LCA
2. if p.val and q.val < node.val, then the LCA must in the left sub-tree of node
3. if p.val and q.val > node.val, then the LCA must in the right sub-tree of node
'''
### TC: O(n) and SC: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def contain(node):
            if node is None:
                return 
            if node.val == p or node.val == q: ### the first time a node's val equals to p or q, it means that the LCA has been found
                return node.val
            elif node.val < p and node.val < q:
                return contain(node.right)
            elif node.val > p and node.val > q:
                return contain(node.left)
            else: ### Trick: if p and q are not in the same side, then we find the LCA
                return node.val
        return contain(root)

### Iterative Version
### TC: O(n) and SC: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            parent_val = node.val
            if node.val == p or node.val == q: ### the first time a node's val equals to p or q, it means that the LCA has been found
                return node.val
            elif node.val < p and node.val < q:   
                node = node.right
            elif node.val > p and node.val > q:
                node = node.left
            else: ### Trick: if p and q are not in the same side, then we find the LCA
                return node.val