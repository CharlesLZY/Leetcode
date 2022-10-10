'''
Leetcode 1696. Jump Game VI

Description:
You are given a 0-indexed integer array nums and an integer k. You are initially standing at index 0. 
In one move, you can jump at most k steps forward without going outside the boundaries of the array. 
That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). 
Your score is the sum of all nums[j] for each index j you visited in the array.
Return the maximum score you can get.
'''

# @param nums List[int]
# @param k int
# @return int

'''
DP[i] means the max score if end at i
DP[i] = max(DP[i-k],...,DP[i-1]) + nums[i]
'''
### Naive DP Solution
### TC: O(nk) and SC: O(n)
class Solution:
    def maxResult(self, nums, k):
        DP_table = [0] * len(nums)
        DP_table[0] = nums[0]
        for i in range(1, len(nums)):
            DP_table[i] = max(DP_table[max(i-k, 0):i]) + nums[i]
        return DP_table[-1]

### Optimized DP Solution
### TC: O(nlogk) and SC: O(n)
from heapq import *
class Solution:
    def maxResult(self, nums, k):
        DP_table = [0] * len(nums)
        DP_table[0] = nums[0]
        maxHeap = []
        heappush(maxHeap, (-nums[0], 0)) ### -value to realize max heap and also store the index
        for i in range(1, len(nums)):
            while maxHeap[0][1] < i-k: ### pop the value beyond the window of size k
                heappop(maxHeap)
            DP_table[i] = nums[i] + DP_table[maxHeap[0][1]]
            heappush(maxHeap, (-DP_table[i], i))
        return DP_table[-1]

### Optimized DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def maxResult(self, nums, k):
        DP_table = [0] * len(nums)
        DP_table[0] = nums[0]
        stack = [0] ### maintain a descending stack
        for i in range(1, len(nums)):
            if stack and stack[0] < i-k:
                stack.pop(0)
            DP_table[i] = DP_table[stack[0]] + nums[i]
            while stack and DP_table[stack[-1]] <= DP_table[i]: ### trick: <= update as soon as possible
                stack.pop()
            stack.append(i)
        return DP_table[-1]
