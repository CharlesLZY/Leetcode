'''
Leetcode 429. N-ary Tree Level Order Traversal

Description:
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Example:
                        1
        2      3                 4        5  
             6   7               8      9   10
                 11             12     13   
                 14
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''

### LC428 Serialize and Deserialize N-ary Tree

# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

# @param root Node
# @return List[List[int]]

### TC: O(n) and SC: O(n)
from collections import deque
class Solution:
    def levelOrder(self, root):
        res = []
        if root is None: ### corner case
            return res
        cur_level = deque([root])
        while cur_level:
            next_level = deque()
            res.append([])
            while cur_level:
                cur = cur_level.popleft()
                if cur:
                    res[-1].append(cur.val)
                    if cur.children:
                        next_level.extend(cur.children)

            cur_level = next_level
        return res

