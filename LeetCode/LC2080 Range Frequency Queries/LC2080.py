'''
Leetcode 2080. Range Frequency Queries

Description:
Design a data structure to find the frequency of a given value in a given subarray.
The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:
- RangeFreqQuery(int[] arr) 
  Constructs an instance of the class with the given 0-indexed integer array arr.
- int query(int left, int right, int value) 
  Returns the frequency of value in the subarray arr[left...right].

A subarray is a contiguous sequence of elements within an array. 
arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).

Example:
RangeFreqQuery: [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
query: [1,  2,  4] return 1
query: [0, 11, 33] return 2
'''

'''
这题是典型的open question, 需要根据你的需求来设计数据结构, space complexity和time complexity的trade off
'''
### TC: O(1) and SC: O(kn) where k is the value number
class RangeFreqQuery:
    def __init__(self, arr):
        self.hashTable = {}
        values = set(arr)
        N = len(arr)
        for v in values:
            self.hashTable[v] = [0]
            cur = 0
            for i in range(N):
                if arr[i] == v:
                    cur += 1
                self.hashTable[v].append(cur)

    def query(self, left, right, value):
        if value in self.hashTable:
            return self.hashTable[value][right+1] - self.hashTable[value][left]
        else:
            return 0


### TC: O(logn) and SC: O(n)
class RangeFreqQuery:
    def __init__(self, arr):
        self.hashTable = {}
        for i in range(len(arr)):
            if arr[i] in self.hashTable:
                self.hashTable[arr[i]].append(i)
            else:
                self.hashTable[arr[i]] = [i]

    ### for searching low bound
    def searchFirstGE(self, arr, idx): ### find first number greater than idx
        lp = 0
        rp = len(arr)-1
        while lp <= rp:
            mid = (lp + rp) // 2
            if arr[mid] >= idx: ### trick
                rp = mid - 1
            else: ### arr[mid] < idx
                lp = mid + 1

        return lp ### arr[lp:] >= idx, if idx > max(arr) return len(arr)

    ### for searching high bound
    def searchFirstLE(self, arr, idx): ### find first number less than idx
        lp = 0
        rp = len(arr)-1
        while lp <= rp:
            mid = (lp + rp) // 2
            if arr[mid] <= idx: ### trick
                lp = mid + 1
            else: ### arr[mid] > idx
                rp = mid - 1

        return rp ### arr[:rp] <= idx, if idx < min(arr) return -1

    def query(self, left, right, value):
        if value not in self.hashTable: ### corner case
            return 0
        arr = self.hashTable[value]
        low = self.searchFirstGE(arr, left)
        high = self.searchFirstLE(arr, right)
        if low == len(arr):
            return 0
        if high == -1:
            return 0
        return high - low + 1

### Brute
### TC: O(n) and SC: O(1) 
class RangeFreqQuery:
    def __init__(self, arr):
        self.arr = arr

    def query(self, left, right, value):
        count = 0
        if 0 <= left < len(self.arr) and 0 <= right < len(self.arr):
            for i in range(left, right+1):
                if self.arr[i] == value:
                    count += 1
        return count