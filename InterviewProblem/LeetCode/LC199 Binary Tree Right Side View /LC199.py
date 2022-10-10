'''
Leetcode 199. Binary Tree Right Side View

Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return List[int]

### BFS Solution
### TC: O(n) and SC: O(D) where D is the diameter of the tree
class Solution:
    def rightSideView(self, root):
        ans = []
        if root:
            queue = [(root, 0)]
            ans.append(root.val)
            while queue:
                cur, depth = queue.pop(0)
                if cur.right:
                    queue.append((cur.right, depth+1))
                if cur.left:
                    queue.append((cur.left, depth+1))
                if queue and queue[0][1] != depth:
                    ans.append(queue[0][0].val)

        return ans

### Better BFS Solution (using None to partition different levels)
### TC: O(n) and SC: O(D) where D is the diameter of the tree
class Solution:
    def rightSideView(self, root):
        ans = []
        if root:
            queue = [root, None]
            ans.append(root.val)
            while queue:
                cur = queue.pop(0)
                if cur == None: ### trick: when we reach the end of current level, nodes in next level have been in the queue
                    if queue: ### if it is not the end of the last level
                        queue.append(None) ### mark the end of the next level
                        ans.append(queue[0].val)
                else:
                    if cur.right:
                        queue.append(cur.right)
                    if cur.left:
                        queue.append(cur.left)

        return ans

### DFS Solution
### TC: O(n) and SC: O(H) where D is the height of the tree
class Solution:
    def rightSideView(self, root):
        ans = []
        def DFS(node, depth):
            if depth == len(ans): ### in this way, we will only append the first occurred node in each level
                ans.append(node.val)
            if node.right:
                DFS(node.right, depth+1)
            if node.left:
                DFS(node.left, depth+1)

        if root:
            DFS(root, 0)
        return ans




