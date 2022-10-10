### lambda arg1, arg2, ... : expersion
### lambda匿名函数，可以接受任意数量的参数，但只能有一个表达式
### 使用场景：你所要做的操作是不重要的(函数不值得起一个名字)
add = lambda x,y : x+y
print(add(1,1))

arr = [3,2,5,1,6,4,0]
# sorted_arr = sorted(arr, key=lambda x: -x)
# sorted_arr = sorted(arr)
# print(sorted_arr)

arr.sort(key=lambda x:-x)
print(arr)

from collections import defaultdict
graph = defaultdict(lambda: set())

### Only __lt__ is needed by Python for sorting
### if we want to use heap for some objects that do not support to compare
### we can re-implement __lt__
class Node:
    def __init__(self, val=-1):
        self.val = val
    def __lt__(self, other): ### less than
        return self.val < other.val

node1 = Node(1)
node2 = Node(2)
from heapq import *
heap = []
heap.append(node2)
heap.append(node1)
heapify(heap)
print(heappop(heap).val)
    