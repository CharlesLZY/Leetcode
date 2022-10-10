'''
JZ38 字符串的排列

描述：
输入一个长度为 n 字符串，打印出该字符串中字符的所有排列，你可以以任意顺序返回这个字符串数组。
'''

# @param string str
# @return List[str]

from collections import Counter

class Solution:
    def Permutation(self , string):
    	ans = []
    	def forward(perm, counter):
    		if len(perm) == len(string):
    			ans.append(perm)
    		else:
    			for char in counter:
    				if counter[char] > 0:
    					counter[char] -= 1
    					forward(perm + char, counter)
    					counter[char] += 1
    	forward("", Counter(string))
    	return ans