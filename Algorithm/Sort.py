'''
float the biggest bubble up (Stable)
'''
### TC: O(n^2) SC: O(1)
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]: ### array[len(array) - i - 1] is current MAX
                array[j], array[j+1] = array[j+1], array[j] ### swap, the bubble float up
'''
select a minimum each time (Unstable)
'''
### TC: O(n^2) SC: O(1)
def selectionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]: ### array[i] is current MIN
                array[i], array[j] = array[j], array[i]

'''
Given a sorted array, each time insert a number (shift the sorted array to the right) (Stable)
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
Find the partition for pivot, the left half is smaller than pivot and the right half is larger than pivot (Unstable)
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
        quickSort(array,low,j-1)
        quickSort(array,j+1, high)

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

'''
Devide and Conquer (Stable)
'''
def mergeSort(arr, aux, low, high): ### temp should be an array has the same length with arr
    def merge(arr, aux, low, high):
        ### copy the orginal array to auxilary array
        for i in range(low, high+1):
            aux[i] = arr[i]

        mid = (low + high) // 2
        p1 = low
        p2 = mid+1
        ### aux[low:mid+1] and aux[mid+1:high] are both sorted
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

'''
Maintain a heap and keep placing the heap top to the array's tail (Unstable)
'''
'''
为什么堆排的空间复杂是O(1)且worst case也是O(nlogn), 却不能取代快排的地位？
1. Locality: 对于快速排序来说, 数据是顺序访问的。而对于堆排序来说, 数据是跳着访的, 对CPU cache不友好。
2. 快速排序数据交换的次数不会比逆序度多, 但堆排序的第一步是建堆，建堆的过程会打乱数据原有的相对先后顺序，导致原数据的有序度降低。
'''
### TC: O(nlogn) and SC: O(1) ### in-place
def heapSort(array):
    def siftDown(idx, arrLen):
        left  = 2*idx + 1 ### left child
        right = 2*idx + 2 ### right child
        least = idx
        if left < arrLen and array[left] < array[least]:
            least = left
        if right < arrLen and array[right] < array[least]:
            least = right

        if least != idx:
            array[idx], array[least] = array[least], array[idx]
            siftDown(least, arrLen)

    def heapify(arrLen):
        leaf = arrLen - 1
        parent = (leaf - 1) // 2
        if parent >= 0:
            for i in range(parent, -1, -1): ### half of the nodes are parent
                siftDown(i, arrLen)

    for i in range(len(array)):
        heapify(len(array)-i)
        array[len(array)-1-i], array[0] = array[0], array[len(array)-1-i]



### Bucket Sort (need extra information)
### TC: O(nlog(n/k)) and SC: O(n+k) sorting k sublist needs k * n/k log(n/k) = nlog(n/k)
def bucketSort(array):
    array = list(map(int, array)) ### for convenience
    k = 10
    buckets = [[] for _ in range(k)]
    lowerBound = min(array)
    upperBound = max(array)
    interval = (upperBound - lowerBound) // k + 1
    for n in array:
        buckets[(n - lowerBound) // interval].append(n) ### split the array to buckets

    res = []
    for bucket in buckets:
        bucket.sort()
        res += bucket

    return res


import random
arr = [random.randint(0,100) for _ in range(20)]
heapSort(arr)
print(arr)
# print*bucketSort(arr)