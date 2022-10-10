'''
Leetcode 170. Two Sum III - Data structure design

Description:
Design a data structure that accepts a stream of integers and checks 
if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:
- TwoSum() Initializes the TwoSum object, with an empty array initially.
- void add(int number) Adds number to the data structure.
- boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, 
  otherwise, it returns false.
'''

### Sorted List Solution
### TC: add O(logn) find O(n) 
class TwoSum:
    def __init__(self):
        self.arr = []

    def add(self, number):
        if len(self.arr) == 0:
            self.arr.append(number)
            return
        if number > self.arr[-1]:
            self.arr.append(number)
            return
        lp = 0
        rp = len(self.arr) - 1
        while lp < rp:
            mid = (lp+rp) // 2
            if self.arr[mid] < number: ### left upper boundary that any number on the left side is smaller than k
                lp = mid+1
            else:
                rp = mid
        self.arr.insert(lp, number)

    def add(self, number):
        if len(self.arr) == 0:
            self.arr.append(number)
            return
        if number < self.arr[0]:
            self.arr.insert(0, number)
            return
        lp = 0
        rp = len(self.arr) - 1
        while lp < rp:
            mid = (lp+rp) // 2 + 1
            if self.arr[mid] < number: ### last number smaller than k
                lp = mid
            else:
                rp = mid-1
        self.arr.insert(lp+1, number)

    def find(self, value):
        lp = 0
        rp = len(self.arr)
        while lp < rp:
            temp = self.arr[lp] + self.arr[rp]
            if temp < value:
                lp += 1
            elif temp > value:
                rp -= 1
            else:
                return True
        return False


### Hash Table Solution
### TC: TC: add O(1) find O(n)
from collections import defaultdict
class TwoSum:
    def __init__(self):
        self.hashTable = {}

    def add(self, number):
        if number in self.hashTable:
            self.hashTable[number] += 1
        else:
            self.hashTable[number] = 1

    def find(self, value):
        for n in self.hashTable.keys():
            complement = value - n
            if complement in self.hashTable:
                if complement == n: ### corner case: if target == 2*n
                    if self.hashTable[n] > 1:
                        return True
                else:
                    return True
        return False
