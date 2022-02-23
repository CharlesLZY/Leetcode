'''
Leetcode 1306. Jump Game III

Description:
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], 
check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''

# @param arr List[int]
# @param start int 
# @return bool

### BFS
### TC: O(n) and SC: O(n)
class Solution:
    def canReach(self, arr, start):
        queue = [start]
        visited = [] ### can be optimized to negative mark
        while queue:
            cur = queue.pop(0)
            if cur in visited:
                continue
            visited.append(cur)

            if arr[cur] == 0:
                return True
            if 0 <= cur + arr[cur] < len(arr):
                queue.append(cur + arr[cur])
            if 0 <= cur - arr[cur] < len(arr):
                queue.append(cur - arr[cur])
        return False

### Better BFS
### TC: O(n) and SC: O(n)
class Solution:
    def canReach(self, arr, start):
        queue = [start]
        while queue:
            cur = queue.pop(0)
            if arr[cur] == -1: ### visited
                continue
            if arr[cur] == 0:
                return True
            if 0 <= cur + arr[cur] < len(arr):
                queue.append(cur + arr[cur])
            if 0 <= cur - arr[cur] < len(arr):
                queue.append(cur - arr[cur])

            arr[cur] = -1 ### mark as visited

        return False

### DFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def canReach(self, arr, start):
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False