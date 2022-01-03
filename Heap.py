'''
A heap is a specialized tree-based data structure which is an almost complete tree that satisfies the heap property:
In a max heap, for any given node C, if P is a parent node of C, then the value of P is greater than or equal to the key of C. 
A common implementation of a heap is the binary heap which is implemented as array for the efficiency. 
Therefore, given a node at index i, its children are at indices 2i+1 and 2i+2, and its parent is at index (i−1) // 2
'''


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
    heap = [] ### min heap

    def siftUp(self, idx):
        if idx > 0: ### still can go up
            parent = (idx - 1) // 2
            if self.heap[idx] < self.heap[parent]: ### if it is larger than parent, then swap 
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                self.siftUp(parent) ### keep sifting up

    def siftDown(self, idx):
        left  = 2*idx + 1 ### left child
        right = 2*idx + 2 ### right child
        if right < len(self.heap):
            if self.heap[right] > self.heap[idx] and self.heap[left] > self.heap[idx]:
                return
            if self.heap[right] < self.heap[left]: ### swap with the smaller child
                self.heap[right], self.heap[idx] = self.heap[idx], self.heap[right] ### swap
                self.siftDown(right) ### keep sifting down
            else:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left] ### swap
                self.siftDown(left) ### keep sifting down
        elif left < len(self.heap):
            if self.heap[left] > self.heap[idx]:
                return
            else:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left] ### swap
                self.siftDown(left) ### keep sifting down

    def push(self, x):
        self.heap.append(x) ### place the new node at the bottom of the heap
        self.siftUp(len(self.heap)-1) ### sift up until the heap property maintains

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
Heap Sort:
Built a heap from the original array.
Keep poping the heap and put the MAX into the bottom.
After all nodes are popped, we will have a new sorted array.
'''
from heapq import * ### min heap
def heapSort(arr):
    heapify(arr)
    sortedArr = []
    for i in range(len(arr)):
        sortedArr.append(heappop(arr))
    return sortedArr