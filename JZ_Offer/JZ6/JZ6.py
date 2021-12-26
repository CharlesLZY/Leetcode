'''
JZ6 从尾到头打印链表

描述：
输入一个链表的头节点，按链表从尾到头的顺序返回每个节点的值（用数组返回）。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param listNode ListNode
# @return List[int]

### TC: O(n) and SC: O(n)
class Solution:
    def __init__(self):
        self.ans = []

    def traverse(self, listNode): ### recursive
        if listNode:
            self.traverse(listNode.next)
            self.ans.append(listNode.val)
        else:
            return

    def printListFromTailToHead(self, listNode):
        self.traverse(listNode)
        return self.ans


class Solution:
    def printListFromTailToHead(self, listNode):
        ans = []
        while listNode:
            ans.append(listNode.val)
        ans.reverse()
        return ans

