'''
A heap is a specialized tree-based data structure which is an almost complete tree that satisfies the heap property:
In a max heap, for any given node C, if P is a parent node of C, then the value of P is greater than or equal to the key of C. 
A common implementation of a heap is the binary heap which is implemented as array for the efficiency. 
Therefore, given a node at index i, its children are at indices 2i+1 and 2i+2, and its parent is at index (i-1) // 2
'''
# from queue import PriorityQueue ### 是用heapq实现的
# heap = PriorityQueue()
# array = [('b', 2), ('a', 1), ('c', 3)]
# for char, p in array:
#     heap.put(char, p)
# while not heap.empty():
#     print(heap.get())

from heapq import * ### only supply min heap, we need to encapsulate our own max heap

class MIN_Heap:
    heap = [] ### min heap
    def __init__(self, array):
        for num in array:
            self.push(num)
    def push(self, x):
        heappush(self.heap, x)
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            return heappop(self.heap)
    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]
    def __len__(self):
        return len(self.heap)

class MAX_Heap:
    heap = [] ### min heap
    def __init__(self, array):
        for num in array:
            self.push(num)

    def push(self, x):
        heappush(self.heap, -x)
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            return -heappop(self.heap)
    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return -self.heap[0]
    def __len__(self):
        return len(self.heap)


class Heap:
    def __init__(self, array=[]):
        self.heap = array
        self.heapify()

    ### TC: O(n) O(n * \sum_{h=0}^{logn} n/2^{h+1} ) 完全二叉树每层n/2^{h+1}个节点
    def heapify(self): ### 对每层（从下往上）根节点做sift down (不用sift up是因为可以无视掉叶子点)
        leaf = len(self.heap) - 1
        parent = (leaf - 1) // 2
        if parent >= 0:
            for i in range(parent, -1, -1): ### half of the nodes are parent
                self.siftDown(i)


    ### TC: O(logn)
    def siftUp(self, idx):
        if idx > 0: ### still can go up
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]: ### if it is larger than parent, then swap 
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                self.siftUp(parent) ### keep sifting up

    ### TC: O(logn)
    def siftDown(self, idx):
        left  = 2*idx + 1 ### left child
        right = 2*idx + 2 ### right child
        least = idx
        if left < len(self.heap) and self.heap[left] < self.heap[least]:
            least = left
        if right < len(self.heap) and self.heap[right] < self.heap[least]:
            least = right

        if least != idx:
            self.heap[idx], self.heap[least] = self.heap[least], self.heap[idx]
            self.siftDown(least)

    ### TC: O(logn)
    def push(self, x):
        self.heap.append(x) ### place the new node at the bottom of the heap
        self.siftUp(len(self.heap)-1) ### sift up until the heap property maintains

    ### TC: O(logn)
    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            top = self.heap[0]
            bottom = self.heap.pop()
            if self.heap:
                self.heap[0] = bottom
                self.siftDown(0)
            return top

    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]

    def __len__(self):
        return len(self.heap)


'''
Heap Sort: TC: O(nlogn) ***SC: O(1)***
Built a heap from the original array.
Keep poping the heap and put the MAX into the bottom.
After all nodes are popped, we will have a new sorted array.
'''
def heapSort(arr):
    heap = Heap(arr)
    sortedArr = []
    for _ in range(len(arr)):
        sortedArr.append(heap.pop())
    return sortedArr


import random
array = [random.randint(0,100) for _ in range(20)]
print(heapSort(array))