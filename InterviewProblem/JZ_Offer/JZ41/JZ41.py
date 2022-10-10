'''
JZ41 数据流中的中位数

描述：
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

Example
Input： [5,2,3,4,1,6,7,0,8]
Output: 5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00
'''


from heapq import * ### only supply min heap, we need to encapsulate our own max heap

class MIN_Heap:
    heap = [] ### min heap
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

### Heap Solution
### TC: O(logn) and SC: O(n)
class Solution:
    maxHeap = MAX_Heap() ### left half
    minHeap = MIN_Heap() ### right half
    def Insert(self, num):
        if len(self.maxHeap) == 0 or num < self.maxHeap.top():
            self.maxHeap.push(num)
        else:
            self.minHeap.push(num)

        ### balance two heaps to ensure the length difference between the two heaps is less than 1
        if len(self.minHeap) == len(self.maxHeap) + 2:
            self.maxHeap.push(self.minHeap.pop())
        elif len(self.minHeap) + 2 == len(self.maxHeap):
            self.minHeap.push(self.maxHeap.pop())


    def GetMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap.top() + self.maxHeap.top()) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap.top()
        else:
            return self.maxHeap.top()






