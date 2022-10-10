'''
Leetcode 234. Palindrome Linked List

Description:
Given the head of a singly linked list, return true if it is a palindrome.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode 
# @return bool

### Intuitive Array Solution
### TC: O(n) and SC: O(n)
class Solution:
    def isPalindrome(self, head):
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes == nodes[::-1]

### Recursion Solution
### TC: O(n) and SC: O(n)
class Solution:
    cur = None
    def isPalindrome(self, head):
        self.cur = head
        def check(node):
            if node is None:
                return True
            if not check(node.next):
                return False
            if node.val == self.cur.val:
                self.cur = self.cur.next
                return True
            else:
                return False
        return check(head)

### Two Pointer Solution (reverse half of the list)
### TC: O(n) and SC: O(1)
class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        '''
        1 2 3 4
            s 
                f
        1 2 3
          s
            f
        '''
        if fast: ### odd length 
            slow = slow.next

        fast = head
        
        def reverse(head):
            dummy = ListNode()
            cur = head
            while cur:
                temp = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = temp
            return dummy.next

        slow = reverse(slow)

        while slow:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
