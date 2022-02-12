'''
Leetcode 987. Vertical Order Traversal of a Binary Tree

Description:
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) 
and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting 
from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. 
In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# @param root TreeNode 
# @return List[List[int]]

'''
We iterate all nodes and get their row, col and value. Sort nodes according their col(from leftmost to rightmost) then row, then value
'''
### Intuitive Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def verticalTraversal(self, root):
        def less(node1, node2): ### node: (val, row, col)
            if node1[2] < node2[2]: ### compare col first
                return True
            elif node1[2] > node2[2]:
                return False
            else:
                if node1[1] < node2[1]: ### then compare row 
                    return True
                elif node1[1] > node2[1]:
                    return False
                else:
                    if node1[0] < node2[0]: ### finally compare value
                        return True
                    else:
                        return False

        def quickSort(arr, low, high):
            if low < high:
                j = low
                pivot = arr[high]
                for i in range(low, high):
                    if less(arr[i], pivot):
                        arr[i], arr[j] = arr[j], arr[i]
                        j += 1

                arr[high], arr[j] = arr[j], arr[high]
                quickSort(arr, low, j-1)
                quickSort(arr, j+1, high)

        nodes = []
        def DFS(node, row, col):
            if node:
                nodes.append((node.val, row, col))
                if node.left:
                    DFS(node.left, row+1, col-1)
                if node.right:
                    DFS(node.right, row+1, col+1)

        DFS(root, 0, 0)
        # nodes.sort(key = lambda x: (x[2], x[1], x[0])) ### compare col first then row then value
        quickSort(nodes, 0, len(nodes)-1)

        ans = []
        for node in nodes:
            if ans and ans[-1][0] == node[2]:
                ans[-1].append(node[0]) ### append node.val
            else:
                ans.append([node[2]]) ### to mark the col
                ans[-1].append(node[0]) ### append node.val

        return [arr[1:] for arr in ans]

### Bucket Sort Solution
### TC: O(nlog(n/k)) and SC: O(n) sorting k sublist needs k * n/k log(n/k) = nlog(n/k)
from collections import *
class Solution:
    def verticalTraversal(self, root):
        nodes = defaultdict(list) ### trick
        minCol = 0 ### bucket index start from minCol
        maxCol = 0 ### bucket index end at minCol

        def DFS(node, row, col):
            nonlocal minCol, maxCol ### trick
            if node:
                nodes[col].append((node.val, row))
                if node.left:
                    minCol = min(minCol, col-1)
                    DFS(node.left, row+1, col-1)
                if node.right:
                    maxCol = max(maxCol, col+1)
                    DFS(node.right, row+1, col+1)

        DFS(root, 0, 0)

        ans = []
        for col in range(minCol, maxCol+1):
            nodes[col].sort(key = lambda x: (x[1], x[0])) ### compare row first then value  
            ans.append([node[0] for node in nodes[col]])
        return ans

