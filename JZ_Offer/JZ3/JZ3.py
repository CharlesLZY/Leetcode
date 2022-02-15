'''
JZ3 数组中重复的数字

描述： 
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，
那么对应的输出是2或者3。存在不合法的输入的话输出-1。
'''

# @param numbers List[int] 
# @return int

### Intuitive Hash Table Solution
### TC: O(n) and SC: O(n)
class Solution:
    def duplicate(self, numbers):
        n = len(numbers)
        if n == 0:
            return -1 ### corner case: input is null
        hashTable = [0]*n
        for i in range(n):
            if numbers[i] >= n:
                return -1
            else:
                if hashTable[numbers[i]] == 0:
                    hashTable[numbers[i]] += 1
                else:
                    return numbers[i]

        return -1 ### no duplicated number


'''
The tricky part of this problem is that all values are in the range [0, n-1], we can use them as index.
'''
### TC: O(n) and SC: O(1)
class Solution:
    def duplicate(self , numbers):
        n = len(numbers)
        if n == 0:
            return -1 ### corner case: input is null
        i = 0
        while i < n: 
            if numbers[i] == i: ### unless the number is in on its own seat, the while lopp will keep swapping 
                i += 1
            else:
                if numbers[i] == numbers[numbers[i]]:
                    return numbers[i]
                else:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]] ### the order of the assignment statement cannot exchange
                    ### i stays the same, because we do not check the number swap to here
        return -1 ### no duplicated number


### Modified the genius solution from leetcode 442
### TC: O(n) and SC: O(1)
class Solution:
    def duplicate(self , numbers):
        if len(numbers) == 0:
            return -1 ### corner case: input is null

        for n in numbers:
            N = abs(n)-1 if n<0 else n
            if numbers[N] < 0:
                return N
            else:
                numbers[N] = -numbers[N] - 1 ### use opposite number to mark whether number is visited
        return -1


### Another method which can record the repeat times
### TC: O(n) and SC: O(1)
class Solution:
    def duplicate(self , numbers):
        L = len(numbers)
        if L == 0:
            return -1 ### corner case: input is null

        repeat = 1 ### repeat times
        for n in numbers:
            N = n % L
            if numbers[N] // L == repeat:
                return N
            else:
                numbers[N] = numbers[N] + L 
        return -1