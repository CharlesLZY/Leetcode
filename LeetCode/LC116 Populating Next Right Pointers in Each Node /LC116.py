'''
Leetcode 116. Populating Next Right Pointers in Each Node

Description:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next

# @param root Node 
# @return Node

### Intuitive BFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def connect(self, root):
        if root is None:
            return None
        else:
            
            queue = [(root, 0)]
            curLevel = []
            while queue:
                cur, depth = queue.pop(0)
                curLevel.append(cur)
                if cur.left:
                    queue.append((cur.left, depth+1))
                if cur.right:
                    queue.append((cur.right, depth+1))
                if queue and queue[0][1] != depth:
                    head = curLevel.pop(0)
                    while curLevel:
                        head.next = curLevel.pop(0)
                        head = head.next
                    
            head = curLevel.pop(0)
            while curLevel:
                head.next = curLevel.pop(0)
                head = head.next
            return root

### Better BFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def connect(self, root):
        if root is None:
            return root
        queue = []
        queue.append(root)
        queue.append(None) ### use None to mark the end of current level
        
        while queue:
            cur = queue.pop(0)
            if cur == None: ### trick: when we reach the end of current level, nodes in next level have been in the queue
                if queue: ### if it is not the end of the last level
                    queue.append(None) ### mark the end of the next level
            else:
                cur.next = queue[0] ### before we meet None, we can ensure that all nodes are in the same level
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root

### Better Solution utilizing previous level
### TC: O(n) and SC: O(1)
class Solution:
    def connect(self, root):
        if root is None:
            return root
        else:
            prevHead = root ### use previous level nodes' next to link current level nodes
            while prevHead.left: ### suppose nodes' nexts are all set in the previous level
                cur = prevHead
                while cur:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                    cur = cur.next
                prevHead = prevHead.left 
            return root










                    