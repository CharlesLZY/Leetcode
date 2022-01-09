'''
Leetcode House Robber III

Description:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house.  
After a tour, the smart thief realized that all houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode
# @return int

### Brute Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def rob(self, root):
        def DFS(node, robParent):
            if node is None:
                return 0
            if not robParent:
                ### even parent is not selected, child can still be not selected
                return max(node.val + DFS(node.left, True) + DFS(node.right, True), DFS(node.left, False) + DFS(node.right, False))
            else:
                return DFS(node.left, False) + DFS(node.right, False)
        return max(DFS(root, False), DFS(root, True))

### Recursion with memoization
### TC: O(n) and SC: O(n)
class Solution:
    def rob(self, root):
        robTable = {}
        notRobTable = {}
        def DFS(node, robParent):
            if node is None:
                return 0
            if not robParent:
                if node in notRobTable:
                    return notRobTable[node]
                ### even parent is not selected, child can still be not selected
                notRobTable[node] = max(node.val + DFS(node.left, True) + DFS(node.right, True), DFS(node.left, False) + DFS(node.right, False))
                return notRobTable[node]
            else:
                if node in robTable:
                    return robTable[node]
                robTable[node] = DFS(node.left, False) + DFS(node.right, False)
                return robTable[node]
        return max(DFS(root, False), DFS(root, True))


'''
The brute solution has tons of replicated computation.
We can return two choices at the same time to reduce recursive call.
'''
### Better Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    def rob(self, root):
        def DFS(node):
            if node is None:
                return (0, 0)
            left = DFS(node.left)
            right = DFS(node.right)
            toRob = node.val + left[1] + right[1]
            notToRob = max(left) + max(right) ### trick: even parent is not selected, child can still be not selected
            return (toRob, notToRob) ### in this way, each node will only visited for once
        return max(DFS(root))


### DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def rob(self, root):
        if not root: ### corner case
            return 0

        nodes = [] ### nodes[i] = value of node i
        graph = {-1: []} ### i : [i's successor]

        queue = [(root, -1)] ### (node, parent_idx)
        idx = 0
        while queue:  ### BFS
            node, parent_idx = queue.pop(0)
            
            nodes.append(node.val)
            graph[idx] = []
            graph[parent_idx].append(idx)

            if node.left:
                queue.append((node.left, idx))
            if node.right:
                queue.append((node.right, idx))
            idx += 1

        robTable = [0] * idx
        notRobTable = [0] * idx

        for i in range(idx-1, -1, -1):
            if not graph[i]:  ### leaf node
                robTable[i] = nodes[i]
                notRobTable[i] = 0
            else:
                robTable[i] = nodes[i] + sum([notRobTable[child] for child in graph[i]])

                notRobTable[i] = sum([max(robTable[child], notRobTable[child]) for child in graph[i]])

        return max(robTable[0], notRobTable[0])

