'''
JZ39 数组中出现次数超过一半的数字

描述：
给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
'''

# @param numbers List[int] 
# @return int


### Intuitive solutions: 1. Hash Table 2. Sort

'''
Candidate Solution:
If a number occupies more than half of the array, it can use the 'perish together' strategy to beat all other numbers.
'''
### TC: O(n) and SC: O(1)
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        condidate = None
        count = 0

        for n in numbers:
            if count == 0:
                condidate = n
                count += 1
            else:
                if condidate != n:
                    count -= 1
                else:
                    count += 1

        winCondition = len(numbers) // 2
        k = 0
        ### check whether the condidate is the mode
        for n in numbers:
            if n == condidate:
                k += 1
            if k >= winCondition:
                return condidate
        return -1 ### there is no number whose occuring times are more than half the length of the array 




