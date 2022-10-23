'''
计算器只支持-1操作和*2操作，初始值x和目标值y，最少通过几步可以从x到y
'''

'''
首先这题，x如果是负数y是正数，则永远不可能到达。所以这题我们假设x,y都是正数。
如果y<x，那么x只能通过-1到达y，如果y>x，那么如果y是奇数，只能通过*2-1这个操作到达，如果y是偶数只能通过*2到达。
步骤都是固定的。
'''
from gettext import dpgettext


def minStep(x, y):
    cur = y
    step = 0
    while cur > x:
        if cur % 2 == 0:
            step += 1
            cur = cur // 2
        else:
            step += 2
            cur = cur // 2 + 1
    step += x - cur
    return step

### DP Solution
def minStep(x, y):
    DP_table = [-1]*(y+2) ### trick: if y is odd, we have to calculate DP[y+1]
    for i in range(min(x+1, y+2)): ### y can be smaller than x
        DP_table[i] = x - i

    for i in range(x+1, y+2):
        if i % 2 == 0:
            DP_table[i] = DP_table[i // 2] + 1
            if DP_table[i-1] == -1: ### update odd number
                DP_table[i-1] = DP_table[i] + 1 

    return DP_table[-2] ### DP table ends at y+1

'''
给定一棵二叉树，最少删除多少节点可以变成一个完全二叉树
'''
class Node:
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root): ### memorized recursion
    H = 0 ### max depth
    hash_table = {} ### (node, max depth of Complete Binary Tree)

    def maxDepth(node):
        nonlocal H
        if node is None:
            return -1
        else:
            if node not in hash_table:
                hash_table[node] = min(maxDepth(node.left), maxDepth(node.right)) + 1
            H = max(hash_table[node], H)
            return hash_table[node]
    
    maxDepth(root)

    return len(hash_table) - (2**(H+1) - 1)


def solution(root): ### postorder traverse (loop version)
    H = 0 ### max depth
    hash_table = {}  ### (node, max depth of Complete Binary Tree)

    def maxDepth(node):
        if node is None:
            return -1
        else:
            return hash_table[node]

    stack = [(root, False)]
    while stack:
        node, done = stack.pop()
        if done:
            h = min(maxDepth(node.left), maxDepth(node.right)) + 1
            H = max(H, h)
            hash_table[node] = h
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    
    return len(hash_table) - (2**(H+1) - 1)

root = Node(val=0)
node1 = Node(val=1)
node2 = Node(val=2)
node3 = Node(val=3)
node3 = Node(val=3)
node4 = Node(val=4)
node5 = Node(val=5)
node6 = Node(val=6)
node7 = Node(val=7)
node8 = Node(val=8)

'''
       0
    1     2 
        3   4
       5 6 7 8
'''
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6
node4.left = node7
node4.right = node8
print(solution(root)) # 2
print(solution(node2)) # 0

'''
       0
          2 
        3   4
       5 6 7 
'''
# root.right = node2
# node2.left = node3
# node2.right = node4
# node3.left = node5
# node3.right = node6
# node4.left = node7
# print(solution(node2)) # 3
# print(solution(root)) # 4

'''
我们定义一个有效序列为：序列两端以外的数一定大于等于最左边的数且大于等于最右边的数
给定一个数组，求它的连续子序列中有多少个有效序列
'''
def solution(nums):
    stack = [nums[0]]
    hash_table = {nums[0]:-1} ### (num: left boundary)
    ans = 0
    for i in range(1, len(nums)):

        prev_h = len(stack)
        while stack and nums[i] < stack[-1]:
            stack.pop()

        lb = len(stack) - 1 ### the rightmost location in the stack where the number is smaller than nums[i]

        if stack and stack[-1] == nums[i]: ### has ancestor
            lb = hash_table[nums[i]] ### use the left boundary of its ancestor
        else: ### new number in the stack
            hash_table[nums[i]] = lb ### update it left boundary
        ans += prev_h - (0 if lb == -1 else lb)
        stack.append(nums[i])
    return ans


'''
给定一个arr(长度为N), 这个arr表示了一颗树(树: 图中的任意2个节点之间有且只有一条路径, 如果我们选定根节点, 树可以看成DAG), 
arr[i] = j表示 Node_(i+1) 和 Node_j 之间有一条边，则这棵树有N+1个结点(因为树的边的数量等于节点数-1) 
求这棵树最多可以拆成几对边?
这样的表示方法, 树的结构不唯一, 因为任何节点都可以看成根节点
E.g.
[0,3,1]
    1      0
   3 0    1 
  2      3
        2
最多可以拆成0-1和2-3

如果把arr[i] = j定义为Node_i的父节点是j(因为树里面映射关系只有父节点, 所以这种方式可以确定树的结构), 
唯一没有父节点的节点就是根节点, 如果我们用-1去表示父节点为空, 那么树的所有节点都可以用arr的index映射(此时树就有N个节点)
E.g.
    0
   3 1
  2
[-1,0,3,0]

    3
  2   0
     1
[3,0,3,-1]

求这棵树的深度？

'''
### 匈牙利算法(先到先得, 能让就让)
### 匈牙利算法用来找二分图(树一定是二分图)的最大匹配
from collections import defaultdict
def solution(arr):
    graph = defaultdict(set)
    for i in range(len(arr)):
        graph[i+1].add(arr[i])
        graph[arr[i]].add(i+1)

    '''
           _ A1 (A1-B2 A1-B3)
          / /
       __/ /
    B2 ---/- A2 (A2-B2)
       __/
    B3 ----- A3 (A3-B3)

    '''
    ### build bi-partite graph (tree must be a bi-partite graph)
    mans = set()
    ladys = set()
    for i in range(len(arr)+1):
        flag = False
        for neighbour in graph[i]:
            if neighbour in mans:
                flag = True
                break
        if flag:
            ladys.add(i)
        else:
            mans.add(i)

    ans = 0
    boyfriends = defaultdict(bool) ### {lady: man}

    ### The Hungarian Algorithm (first come first get, yield if there is backup)
    def canYield(lady):
        cur = boyfriends[lady]
        for neighbour in graph[cur]:
            if boyfriends[neighbour] is False: ### still single
                return neighbour ### we find the backup
        return -1 ### can not find any backup

    for man in mans:
        for neighbour in graph[man]:
            if boyfriends[neighbour] is False: ### still single
                boyfriends[neighbour] = man
                ans += 1
                break
            
            backup = canYield(neighbour) 
            if backup != -1: ### neighbour's boyfriend has backup
                boyfriends[backup] = boyfriends[neighbour] ### neighbour's boyfriend break up with her and find a new girlfriend
                boyfriends[neighbour] = man ### update neighbour's bodyfriend
                ans += 1
                break

    return ans

'''
         0
      1     8
   2    7
 3   4 
5 6
'''
arr = [0,1,2,2,3,3,1,0] ### 4
# arr = [0,1,2,2,3,3] ### 3
# arr = [0,3,1] ### 2
print(solution(arr))


### recursive solution
def depth(arr):
    hash_table = {-1: -1} ### {node: depth}
    def backtrack(node):
        if node in hash_table:
            return hash_table[node]
        else:
            hash_table[node] = backtrack(arr[node]) + 1
            return hash_table[node]


    ans = 0
    for i in range(len(arr)):
        ans = max(ans, backtrack(i))
    return ans

### iterative solution
def depth(arr):
    hash_table = {-1: -1} ### {node: depth}
    ans = 0
    for i in range(len(arr)):
        cur = i
        cur_path = []
        while cur not in hash_table:
            cur_path.append(cur)
            cur = arr[cur]
        cur_depth = hash_table[cur]
        for node in cur_path[::-1]:
            cur_depth += 1
            hash_table[node] = cur_depth
        ans = max(ans, cur_depth)
    return ans


'''
    3
  2   0
     1
[3,0,3,-1]

         0
      1     8
   2    7
 3   4 
5 6
[-1,0,1,2,2,3,3,1,0] 
'''

arr = [3,0,3,-1] # 2
arr = [-1,0,1,2,2,3,3,1,0]  # 4
print(depth(arr))

### Complementary Pairs
'''
A pair of strings form a complementary pair if there is some permutation of their concatenation
that is a palindrome e.g. "abac" and "cab". Give an array of n strings, find the number of
complementary pairs that can be formed.
'''
from collections import Counter, defaultdict
def solution(words):
    bitmasks = []
    for word in words:
        bitmask = 0
        for char in word:
            bitmask ^= (1<<(ord(char) - ord('a')))
        bitmasks.append(bitmask)
    # print(list(map(bin, bitmasks)))
    ans = 0
    for i in range(len(bitmasks)):
        for j in range(i+1, len(bitmasks)):
            concat = bitmasks[i] ^ bitmasks[j]
            if concat == 0:
                ans += 1
            elif Counter(bin(concat))['1'] == 1:
                print(i,j)
                ans += 1
    return ans
    
def solution(words):
    hash_table = defaultdict(int)
    ans = 0
    for word in words:
        bitmask = 0
        for char in word:
            bitmask ^= (1 << (ord(char) - ord('a')))
        ans += hash_table[bitmask]
        num = 1
        for i in range(26): ### 26 English letters
            ans += hash_table[bitmask ^ num]
            num <<= 1
        hash_table[bitmask] += 1
        
    return ans 

arr = ["abc", "abcd", "bc", "adc"] ### ans = 3 "abc"&"abcd"; "abc"&"bc"; "abcd"&"adc"
print(solution(arr))