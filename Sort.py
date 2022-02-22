'''
float the biggest bubble up
'''
### TC: O(n^2) SC: O(1)
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] ### swap, the bubble float up
'''
select a minimum each time
'''
### TC: O(n^2) SC: O(1)
def selectionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

'''
Given a sorted array, each time insert a number (shift the sorted array to the right)
'''
### TC: O(n^2) SC: O(1)
def insertSort(array):
    i = 0 ### the first number can be considered as a sorted array
    for i in range(1, len(array)):
        pivot = array[i]
        j = i - 1
        while j >= 0 and array[j] > pivot: ### trick: until find the position or reach the left end
            array[j+1] = array[j] ### shift to the right
            j -= 1 ### keep compare to the number on the left
        array[j+1] = pivot

'''
Find the partition for pivot, the left half is smaller than pivot and the right half is larger than pivot
'''
def quickSort(array, low, high):
    if low < high:
        import random
        r = random.randint(low, high)
        array[r], array[high] = array[high], array[r]
        
        pivot = array[high]
        j = low ### j the first number which is larger than pivot but on the left side
        for i in range(low, high):
            if array[i] < pivot:
                array[j], array[i] = array[i], array[j]
                j += 1 ### only update when meet number smaller than pivot
        array[j], array[high] = array[high], array[j]
        QuickSort(array,low,j-1)
        QuickSort(array,j+1, high)

### Non-recursive Version of Quick Sort (Simulate the stack)
def quickSort(arr):
    
    stack = [(0, len(arr)-1)] ### simulate the stack, initialize the first call
    while stack:
        low, high = stack.pop(0)
        if low < high:
            pivot = arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
            arr[high], arr[j] = arr[j], arr[high]
            stack.append((low, j-1))
            stack.append((j+1, high))



def mergeSort(arr, aux, low, high): ### temp should be an array has the same length with arr
    def merge(arr, aux, low, high):
        ### copy the orginal array to auxilary array
        for i in range(low, high+1):
            aux[i] = arr[i]

        mid = (low + high) // 2
        p1 = low
        p2 = mid+1
        for i in range(low, high+1):
            if p1 <= mid and p2 <= high:
                if aux[p1] < aux[p2]:
                    arr[i] = aux[p1]
                    p1 += 1
                else:
                    arr[i] = aux[p2]
                    p2 += 1
            elif p1 <= mid:
                arr[i] = aux[p1]
                p1 += 1
            else:
                arr[i] = aux[p2]
                p2 += 1

    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, aux, low, mid)
        mergeSort(arr, aux, mid+1, high)
        merge(arr, aux, low, high)



from heapq import * ### min heap
def heapSort(array):
    heapify(array)
    sortedArr = []
    for i in range(len(arr)):
        sortedArr.append(heappop(arr))
    return sortedArr

class minHeap:
    def __init__(self, array=[]):
        self.heap = array
        self.heapify()

    ### TC: O(n) 一共n/2个根节点，每个节点最多交换2次
    def heapify(self): ### 对每层（从下往上）根节点做sift down (不用sift up是因为，可以无视掉叶子点)
        leaf = len(self.heap) - 1
        parent = (leaf - 1) // 2
        if parent >= 0:
            for i in range(parent, -1, -1): ### trick : there are n/2 root nodes
                self.siftDown(i)

    def siftUp(self,idx):
        if idx > 0:
            parent = (idx - 1) // 2
            if parent >= 0:
                if self.heap[parent] > self.heap[idx]:
                    self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent] ### swap
                    self.siftUp(parent)

    def siftDown(self, idx):
        left  = 2*idx + 1
        right = 2*idx + 2
        if right < len(self.heap):
            if self.heap[left] >= self.heap[idx] and self.heap[right] >= self.heap[idx]:
                return
            
            if self.heap[left] > self.heap[right]: ### swap with the smaller one, because smaller number should on the upper in min heap 
                self.heap[right], self.heap[idx] = self.heap[idx], self.heap[right] ### swap
                self.siftDown(right)
            else:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left] ### swap
                self.siftDown(left)


        elif left < len(self.heap):
            if self.heap[left] >= self.heap[idx]:
                return
            else:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left] ### swap
                self.siftDown(left) ### keep sifting down

    def push(self, x):
        self.heap.append(x)
        self.siftUp(len(self.heap)-1)

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


def heapSort(array):
    heap = minHeap(array)
    sortedArr = []
    for i in range(len(array)):
        sortedArr.append(heap.pop())
    return sortedArr
    
