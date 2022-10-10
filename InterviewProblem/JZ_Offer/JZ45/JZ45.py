'''
JZ45 把数组排成最小的数

描述：
输入一个非负整数数组numbers，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。
1.输出结果可能非常大，所以你需要返回一个字符串而不是整数
2.拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
'''

# @param numbers List[int] 
# @return str

### TC: O(nlogn) and SC: O(n)
import functools ### python3 cancel the sort(cmp = lambda x,y f(x,y))
def cmp(a,b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0

class Solution:
    def PrintMinNumber(self, numbers):
        strings = [str(n) for n in numbers]
        strings.sort(key=functools.cmp_to_key(cmp))
        return ''.join(strings)