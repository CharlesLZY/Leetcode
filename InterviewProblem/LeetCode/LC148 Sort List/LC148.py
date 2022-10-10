'''
Leetcode 148. Sort List

Description:
Given the head of a linked list, return the list after sorting it in ascending order.
'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# @param head ListNode
# @return ListNode

### Merge Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def sortList(self, head):
        def merge(l1, l2):
            dummy = ListNode()
            cur = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next=l1
                    l1=l1.next
                cur = cur.next
            if l1:
                cur.next=l1
            if l2:
                cur.next=l2
            return dummy.next

        def mergeSort(head):
            if head and head.next:
                ### find middle point
                slow = head
                fast = head
                prev = None ### trick
                while fast and fast.next:
                    prev = slow
                    fast = fast.next.next
                    slow = slow.next
                prev.next = None ### trick: must cut the whole list into two lists
                return merge(mergeSort(head), mergeSort(slow)) ### middle must use slow rather than slow.next, if use slow.next will failed in length=2

            else: ### the length of the linked list <= 1
                return head 

        return mergeSort(head)


### Merge Sort (Easy to understand version)
def mergeSort(arr):
    def merge(arr1, arr2):
        merged = [None] * (len(arr1) + len(arr2))
        p1 = 0
        p2 = 0
        for i in range(len(arr1)+len(arr2)):
            if p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    merged[i] = arr1[p1]
                    p1 += 1
                else:
                    merged[i] = arr2[p2]
                    p2 += 1

            elif p1 < len(arr1):
                merged[i] = arr1[p1]
                p1 += 1
            else:
                merged[i] = arr2[p2]
                p2 += 1
        return merged

    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))

### Merge Sort Standard Verison
def mergeSort(arr, temp, low, high): ### temp should be an array has the same length with arr
    def merge(arr, temp, low, high):
        for i in range(low, high+1):
            temp[i] = arr[i] ### temporarily store the array for convenience to merge

        mid = (low + high) // 2
        p1 = low
        p2 = mid + 1
        for i in range(low, high+1):
            if p1 <= mid and p2 <= high:
                if temp[p1] < temp[p2]:
                    arr[i] = temp[p1]
                    p1 += 1
                else:
                    arr[i] = temp[p2]
                    p2 += 1
            elif p1 <= mid:
                arr[i] = temp[p1]
                p1 += 1
            else:
                arr[i] = temp[p2]
                p2 += 1

    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, temp, low, mid)
        mergeSort(arr, temp, mid+1, high)
        merge(arr, temp, low, mid, high)