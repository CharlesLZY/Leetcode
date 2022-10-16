'''
Leetcode 769. Max Chunks To Make Sorted

Description:
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.
'''

# @param arr List[int]
# @return int

### Monotonic Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def maxChunksToSorted(self, arr):
        stack = []
        for n in arr:
            curMin, curMax = n, n ### the number itself can be considered as a partition

            # While the current partition's min is smaller than previous partition's max
            while stack and stack[-1][1] >= curMin:
                ### merge two partitions
                curMin, curMax = min(curMin, stack[-1][0]), max(curMax, stack[-1][1])
                stack.pop()

            stack.append((curMin, curMax))

        return len(stack)

### Greedy Solution (If there is no repeated number in the array)
### TC: O(nlogn) and SC: O(n)
class Solution:
    def maxChunksToSorted(self, arr):
        arr_copy = arr[:]
        arr_copy.sort()
        hash_table = {}
        for i in range(len(arr_copy)):
            hash_table[arr_copy[i]] = i
        
        count = 0
        curMaxIdx = 0
        for i in range(len(arr)):
            curMaxIdx = max(curMaxIdx, hash_table[arr[i]])
            if curMaxIdx == i: ###
                count += 1
        
        return count

### Optimized Greedy Solution
### In this problem, the array is a permutation of [0, n - 1]. We can optimize the solution above.
### TC: O(n) and SC: O(1)
class Solution:
    def maxChunksToSorted(self, arr):
        count = 0
        curMax = arr[0]
        for i in range(len(arr)):
            curMax = max(curMax, arr[i])
            if curMax == i:
                count+=1
                
        return count