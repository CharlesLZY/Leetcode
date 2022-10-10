'''
Leetcode 173. Binary Search Tree Iterator

Description:
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
  The root of the BST is given as part of the constructor. 
  The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, 
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. 
That is, there will be at least a next number in the in-order traversal when next() is called.

Follow up:
Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, 
where h is the height of the tree?
'''

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
The intuitive method is store the inorder traverse so that it can easily achieve O(1) next operation
But if we want O(h) space complexity, we can not use this method.
'''

### TC: O(n) and SC: O(n)
class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.leftmost(root)

    def leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        cur = self.stack.pop()
        self.leftmost(cur.right)
        return cur.val

    def hasNext(self):
        if self.stack:
            return True
        else:
            return False








