'''
JZ56 数组中只出现一次的两个数字

描述：
一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

提示：输出时按非降序排列。
'''

# @param array List[int]
# @return List[int]

### Intuitive Solution: Hash Table: TC: O(n) but SC: O(n) and Sort: SC: O(1) but TC: O(nlogn)
class Solution:
    def FindNumsAppearOnce(self, array):
        hashTable = {}
        for num in array:
            if num in hashTable:
                hashTable[num] += 1
            else:
                hashTable[num] = 1
        ans = []
        for num in hashTable:
            if hashTable[num] == 1:
                ans.append(num)
        return sorted(ans)


'''
A XOR 0 = A
A XOR A = 0
A XOR B = B XOR A
(A XOR B) XOR C = A XOR (B XOR C) 
'''
### If there is only one number occurs once(LC136), we can use XOR to achieve TC O(n) and SC O(1)
def findNumsAppearOnce(array):
    res = 0
    for num in array:
        res ^= num
    return res
