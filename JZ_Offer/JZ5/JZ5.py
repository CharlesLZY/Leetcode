'''
JZ4 二维数组中的查找

描述：
请实现一个函数，将一个字符串s中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# @param s string
# @return string

### TC: O(n) and SC: O(n)
class Solution:
    def replaceSpace(self, s):
        chars = s.split(' ')
        return "%20".join(chars)