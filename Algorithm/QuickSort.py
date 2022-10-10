'''
Quick Sort
TC: Best case O(nlogn) Worst case O(n^2)
SC: Best case O(logn) Worst case O(n) ###其实是看最少要递归多少次, 因为inplace的实现不考虑递归对栈的消耗, SC就是O(1)
Space complexity is determined by the times of recursion.
Tail recursion will not expand extra space because it does not need to store the context to rusume previous codes.

When Does the Worst Case of Quicksort Occur?
Quicksort works by dividing an array into smaller arrays and then sorting those smaller arrays. 
A pivot element is used to partition an array into smaller arrays; 
smaller arrays are divided recursively until an array with only one or no elements is created. 
Hence, the selection of the pivot element plays an important role in the efficiency of the quicksort algorithm.

But when the pivot element divides the array into two unbalanced sub-arrays (huge difference in size), 
the performance of quicksort decreases. Following are the cases where the pivot divides an array into two unbalanced sub-arrays: 

- When the input array is already sorted, and we choose the leftmost element as the pivot element. 
  In this case, we’ll have two extremely unbalanced arrays. One array will have 0 elements, and the other one will have N - 1 elements.

- When the given array is reverse sorted, and we choose the rightmost element as the pivot element. 
  Again, in this case, the pivot elements will split the input array into two unbalanced arrays of size 0 and N - 1.

- When all the elements in the given array are the same. In such a scenario, the pivot element divides the array into one subarray of length N-1, 
  and the time complexity of Quicksort increases significantly.

FAQs Related Quicksort Worst Case
Question 1: Can quicksort be implemented in O(NLogN) worst-case time complexity?

Answer: Yes, we can minimize the worst-case time complexity of quicksort to O(N*logN) by 
finding the median of the unsorted array in O(N) and using the median as the pivot. 
By doing this, we make sure that the array is divided into two subarrays of almost equal size, 
and we never encounter the case when the array is divided into subarrays of size 0 and N-1. 
But the constant factor of this method is very high, and therefore, it is not used in practice.

Question 2: Despite having a worst-case time complexity of O(N^2), why is quicksort considered a fast sorting algorithm?

Answer: The worst case of quicksort O(N^2) can be easily avoided with a high probability by choosing the right pivot. 
Obtaining an average-case behavior by choosing the right pivot element makes the performance better and as efficient as merge sort. 
Quicksort, in particular, exhibits good cache locality, which makes it faster than merge sort in many cases, such as in a virtual memory environment.
'''




'''
Pivot 选头/尾，（先）遍历的方向就得从另外一头开始，因为最终指针停下的位置要和pivot交换
得保证比pivot大/小
'''

'''
Initial array:
Pivot is on the right, start from left
 i
[4        1         0         5         2         3]
 j                                              pivot

arr[i] > pivot: move on, waiting for a value smaller than pivot and then swap with it

          i
[4        1         0         5         2         3]
 j                                              pivot

arr[i] < pivot: swap with arr[j] (the leftmost value larger than pivot), j++, move on

                    i
[1        4         0         5         2         3]
          j                                     pivot

arr[i] < pivot: swap with arr[j] (the leftmost value larger than pivot), j++, move on

                              i
[1        0         4         5         2         3]
                    j                           pivot

arr[i] > pivot: move on, waiting for a value smaller than pivot and then swap with it
                                        i
[1        0         4         5         2         3]
                    j                           pivot

arr[i] < pivot: swap with arr[j] (the leftmost value larger than pivot), j++, move on

                                                  i
[1        0         2         5         4         3]
                              j                 pivot

swap arr[high] and arr[j]

                            pivot                 i
[1        0         2         3         4         5]
                              j                  

'''
import random 
def QuickSort(arr, low, high):
    if low < high:
        r = random.randint(low, high) ### avoid worst case
        arr[high], arr[r] = arr[r], arr[high]

        pivot = arr[high]
        ### j the first number which is larger than pivot but on the left side
        j = low ### must start from the other side (different from the pivot side)
        for i in range(low, high): ### pivot is arr[high], so we pass over arr[high]
            if arr[i] < pivot:
                arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                j += 1 ### only update when meet number smaller than pivot

        arr[j], arr[high] = arr[high], arr[j] ### swap pivot and arr[j]
        QuickSort(arr,low,j-1)
        QuickSort(arr,j+1, high)

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


import random
def QuickSort(arr, low, high):
    if low < high:
        r = random.randint(low, high) ### avoid worst case
        arr[low], arr[r] = arr[r], arr[low]

        pivot = arr[low]
        ### j the first number which is smaller than pivot but on the right side
        j = high ### must start from the other side (different from the pivot side)
        for i in range(high, low, -1): ### pivot is arr[low], so we pass over arr[low]
            if arr[i] > pivot:
                arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                j -= 1 ### from right to left

        arr[j], arr[low] = arr[low], arr[j] ### swap pivot and arr[j]
        QuickSort(arr,low,j-1)
        QuickSort(arr,j+1, high)


'''
To make the process more clear, we use swap verison
Initial array: 
Pivot is on the right, start from left
 lp                                               rp
[4        1         0         5         2         3]
                                                pivot

arr[lp] > pivot: swap arr[lp] and arr[rp], go to the other side
 lp                                               rp
[3        1         0         5         2         4]
pivot                                               

arr[rp] > pivot: rp -= 1
 lp                                     rp         
[3        1         0         5         2         4]
pivot 

arr[rp] < pivot: swap arr[rp] and arr[lp], go to the other side
 lp                                     rp         
[2        1         0         5         3         4]
                                      pivot 
arr[lp] < pivot: lp += 1
          lp                            rp         
[2        1         0         5         3         4]
                                      pivot 

arr[lp] < pivot: lp += 1
                    lp                  rp         
[2        1         0         5         3         4]
                                      pivot 

arr[lp] < pivot: lp += 1
                              lp        rp         
[2        1         0         5         3         4]
                                      pivot 

arr[lp] > pivot: swap arr[lp] and arr[rp], go to the other side
                              lp        rp         
[2        1         0         3         5         4]
                            pivot

arr[rp] > pivot: rp -= 1
                              rp
                              lp                 
[2        1         0         3         5         4]
                            pivot

lp and rp come across
'''

### swap version, more clearly show how pivot moves
import random
def QuickSort(arr, low, high):
    if low < high:
        r = random.randint(low, high) ### avoid worst case
        arr[high], arr[r] = arr[r], arr[high]

        pivot = arr[high]
        lp = low
        rp = high ### must set at pivot location
        while lp < rp:
            while lp < rp and arr[lp] < pivot: ### must start from the other side (different from the pivot side)
                lp += 1
            arr[rp], arr[lp] = arr[lp], arr[rp]

            while lp < rp and arr[rp] >= pivot:
                rp -= 1
            arr[lp], arr[rp] = arr[rp], arr[lp]
        QuickSort(arr,low,lp-1)
        QuickSort(arr,lp+1, high)


'''
Non-swap version
Initial array: 
Pivot is on the right, start from left
 lp                                               rp
[4        1         0         5         2         3]
                                                pivot

arr[lp] > pivot: arr[rp] = arr[lp], go to the other side
 lp                                               rp
[4        1         0         5         2         4]
(pivot                                              

arr[rp] > pivot: rp -= 1
 lp                                     rp         
[4        1         0         5         2         4]
 

arr[rp] < pivot: arr[lp] = arr[rp], go to the other side
 lp                                     rp         
[2        1         0         5         2         4]
                                       
arr[lp] < pivot: lp += 1
          lp                            rp         
[2        1         0         5         2         4]
                                       

arr[lp] < pivot: lp += 1
                    lp                  rp         
[2        1         0         5         2         4]
                                       

arr[lp] < pivot: lp += 1
                              lp        rp         
[2        1         0         5         2         4]
                                       

arr[lp] > pivot: arr[rp] = arr[lp], go to the other side
                              lp        rp         
[2        1         0         5         5         4]
                            

arr[rp] > pivot: rp -= 1
                              rp
                              lp                 
[2        1         0         3         5         4]
                            

lp and rp come across, assign pivot
'''

import random
def QuickSort(arr, low, high):
    if low < high:
        r = random.randint(low, high) ### avoid worst case
        arr[low], arr[r] = arr[r], arr[low]
        pivot = arr[low]
        lp = low ### must set at pivot location
        rp = high
        while lp < rp:
            while lp < rp and arr[rp] > pivot: ### must start from the other side (different from the pivot side)
                rp -= 1
            arr[lp] = arr[rp] ### if we don't swap here, we have to assign pivot when lp and rp come across
            while lp < rp and arr[lp] <= pivot:
                lp += 1
            arr[rp] = arr[lp] ### if we don't swap here, we have to assign pivot when lp and rp come across
        arr[lp] = pivot ### assign pivot
        QuickSort(arr,low,lp-1)
        QuickSort(arr,lp+1, high)



### TC: O(n) Quick select k-th largest number n + n/2 + n/4 + n/8 + ... = 2n
import random
def QuickSelect(arr, k):  ### quick select k-th largest
    def partition(low, high):
        if low < high:
            r = random.randint(low, high) ### avoid worst case
            arr[high], arr[r] = arr[r], arr[high]
            pivot = arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                    j += 1
            arr[j], arr[high] = arr[high], arr[j] 
            return j
        else:
            return low

    ### rank:  len(arr)  ... 2, 1
    ### idx:   0, 1 ... len(arr) - 2, len(arr) - 1
    def select(low, high):
        pivot_index = partition(low, high)
        if len(arr) - k == pivot_index:
            return arr[pivot_index]
        elif len(arr) - k < pivot_index:
            return select(low, pivot_index - 1)
        else:
            return select(pivot_index + 1, high)

    return select(0, len(arr) - 1)


def QuickSelect(arr, k):  ### quick select k-th smallest
    def partition(low, high):
        if low < high:
            pivot = arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                    j += 1
            arr[j], arr[high] = arr[high], arr[j] 
            return j
        else:
            return low

    ### rank:  1, 2 ... len(arr) 
    ### idx:   0, 1 ... len(arr) - 1
    def select(low, high):
        pivot_index = partition(low, high)
        if k-1 == pivot_index:
            return arr[pivot_index]
        elif k-1 < pivot_index:
            return select(low, pivot_index - 1)
        else:
            return select(pivot_index + 1, high)

    return select(0, len(arr) - 1)


### Iterative Version
### TC: O(n) and SC: O(1)
import random
def QuickSelect(arr, k):  ### quick select k-th largest
    def partition(low, high):
        if low < high:
            r = random.randint(low, high) ### avoid worst case
            arr[high], arr[r] = arr[r], arr[high]
            pivot = arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                    j += 1
            arr[j], arr[high] = arr[high], arr[j] 
            return j
        else:
            return low

    ### rank:  len(arr)  ... 2, 1
    ### idx:   0, 1 ... len(arr) - 2, len(arr) - 1
    def select(low, high):
        while low <= high:
            p = partition(low, high)
            if p == len(arr) - k:
                return arr[p]
            elif p < len(arr) - k:
                low = p + 1
            else:
                high = p - 1

    return select(0, len(arr) - 1)