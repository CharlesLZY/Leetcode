'''
JZ8 二叉树的下一个结点

描述：
给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
'''

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

### TC: O(n) and SC: O(n)
class Solution:
    def GetNext(self, pNode):
        inorder_arr = []
        def inorder(root):
            if root:
                inorder(root.left)
                inorder_arr.append(root)
                inorder(root.right)
        temp = pNode
        while temp.next: ### initialize to the root first
            temp = temp.next

        inorder(temp)

        for i in range(len(inorder_arr)-1):
            if inorder_arr[i].val == pNode.val:
                return inorder_arr[i+1]

'''
         7
       /   \
      2     8
     / \
    1   6
       /
      3
       \
        4
         \
          5

[2, 3, 4, 7]: has right child => leftmost child of its right sub-tree

[1]: left child => father
[5, 6]: right child => first parent which is a left child
These two kinds are basically the same


[8]: else => null
'''

### TC: O(n) and SC: O(1)
class Solution:
    def GetNext(self, pNode):
        if pNode:
            if pNode.right:
                temp = pNode.right
                while temp.left:
                    temp = temp.left
                return temp
            else:
                while pNode.next: ### while still have parent
                    ### the first parent which is a left child
                    if pNode.next.left and pNode.next.left.val == pNode.val: ### pnode is the left child of pnode.next
                        return pNode.next
                    pNode = pNode.next



