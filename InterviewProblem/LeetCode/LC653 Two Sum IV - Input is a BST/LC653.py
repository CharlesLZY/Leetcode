'''
Leetcode 653. Two Sum IV - Input is a BST

Description:
Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that their sum is equal to the given target.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @param k int 
# @return bool

### Hash Set Solution
### TC: O(n) and SC: O(n)
class Solution:
    def findTarget(self, root, k):
        hashSet = set()
        queue = [root] ### BFS
        while queue:
            node = queue.pop(0)
            if k - node.val in hashSet:
                return True
            hashSet.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

### Sorted List Solution
### TC: O(n) and SC: O(n)
class Solution:
    def findTarget(self, root, k):
        arr = []
        def inorder(node):
            if node:
                inorder(node.left)
                arr.append(node.val)
                inorder(node.right)
        inorder(root) ### inorder traverse of BST is a sorted array
        lp = 0
        rp = len(arr)-1
        while lp < rp:
            temp = arr[lp] + arr[rp]
            if temp == k:
                return True
            elif temp < k:
                lp += 1
            else:
                rp -= 1
        return False
