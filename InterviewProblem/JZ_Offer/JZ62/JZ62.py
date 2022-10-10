'''
JZ62 孩子们的游戏(圆圈中最后剩下的数)

描述:
每年六一儿童节，牛客都会准备一些小礼物和小游戏去看望孤儿院的孩子们。其中，有个游戏是这样的：
首先，让 n 个小朋友们围成一个大圈，小朋友们的编号是0~n-1。然后，随机指定一个数 m ，
让编号为0的小朋友开始报数。每次喊到 m-1 的那个小朋友要出列唱首歌，然后可以在礼品箱中任意的挑选礼物，
并且不再回到圈中，从他的下一个小朋友开始，继续0... m-1报数....这样下去....直到剩下最后一个小朋友，可以不用表演，
并且拿到牛客礼品，请你试着想下，哪个小朋友会得到这份礼品呢？
'''

# @param n int
# @param m int
# @return int


### Linked List Solution
### TC: O(n^2) and SC: O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0:
            return -1

        head = ListNode(0)
        cur = head
        for i in range(1, n):
            cur.next = ListNode(i)
            cur = cur.next
        cur.next = head ### make cycle

        prev = cur
        cur = head ### start from head
        for i in range(n-1):
            prev = cur
            for j in range(m-1):
                prev, cur = cur, cur.next
            prev.next = cur.next
            cur = cur.next
        return cur.val



'''
假设最开始 n > m
那么第一个出去的是编号m-1的小朋友
新的一轮可以看成同样的问题，
只不过从编号m的小朋友重新开始报数（编号为m的小朋友在新的一轮视为编号0），每个人的编号会存在一个映射关系
原编号f(n,m)  新编号f(n-1,m)
    m   -> 0
    m+1 -> 1
       ...
    n-2 -> n-m-2
    n-1 -> n-m-1
    1   -> n-m
       ...
    m-3 -> n-3
    m-2 -> n-2

可以发现f(n,m) = (f(n-1,m) + m % n) % n
%n 这个操作是把
'''

### TC: O(n) and SC: O(n)
class Solution:
    def LastRemaining_Solution(self, n, m):
        def idx(n,m): ### the last people who will be left
            if n <= 1:
                return 0
            else:
                return (idx(n-1,m) + m % n) % n
        if n == 0: ### corner case
            return - 1
        else:
            return idx(n,m)

### TC: O(n) and SC: O(1)
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0: ### corner case
            return -1
        idx = 0
        for i in range(2, n+1):
            idx = (idx + m) % i
        return idx
