'''
JZ49 丑数

描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第 n个丑数。
'''

# @param index int
# @return int

'''
Ugly Number: 2^x*3^y*5^z
'''

class Solution:
    def GetUglyNumber_Solution(self, index):
        ### the first 6 ugly number: 1 2 3 4 5 6
        if index <= 6:
            return index

        res = [1]
        p_2 = 0 ### which res factor 2 should multiply
        p_3 = 0 ### which res factor 3 should multiply
        p_5 = 0 ### which res factor 5 should multiply


        ### uglyNum = 2^p_2 * 3^p_3 * 5^p_5

        for i in range(1, index):
            nextUglyNum = min(res[p_2]*2, res[p_3]*3, res[p_5]*5)
            if nextUglyNum == res[p_2]*2: ### cannot use if else, must use three if to pass over duplicate uglyNum
                p_2 += 1
            if nextUglyNum == res[p_3]*3: ### cannot use if else, must use three if to pass over duplicate uglyNum
                p_3 += 1
            if nextUglyNum == res[p_5]*5: ### cannot use if else, must use three if to pass over duplicate uglyNum
                p_5 += 1
            
            res.append(nextUglyNum)

        return res[-1]



