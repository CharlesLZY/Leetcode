'''
JZ54 二叉搜索树的第k个节点


描述：
给定一棵结点数为n 二叉搜索树，请找出其中的第 k 小的TreeNode结点值。
1.返回第k小的节点值即可
2.不能查找的情况，如二叉树为空，则返回-1，或者k大于n等等，也返回-1
3.保证n个节点的值不一样
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# @param proot TreeNode
# @param k int
# @return int

### TC: O(n) and SC: O(n)
class Solution:
    n = 0
    def KthNode(self, proot, k):
        self.n = 0
        def inorder(root):
            if root:
                temp = inorder(root.left)
                if temp != -1:
                    return temp
                self.n += 1
                if self.n == k:
                    return root.val
                temp = inorder(root.right)
                if temp != -1:
                    return temp
            return -1
        return inorder(proot)


### Non-recursive version
class Solution:
    def KthNode(self, proot, k):
        if proot:
            n = 0
            stack = [proot]
            nextToVisit = proot

            while stack:
                while nextToVisit.left:
                    stack.append(nextToVisit.left)
                    nextToVisit = nextToVisit.left

                cur = stack.pop()
                n += 1
                if n == k:
                    return cur.val

                if cur.right:
                    stack.append(cur.right)
                    nextToVisit = cur.right

        return -1