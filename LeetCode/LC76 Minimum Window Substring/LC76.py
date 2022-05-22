'''
Leetcode 76. Minimum Window Substring

Description:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s 
such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''

# @param s str 
# @param t str 
# @return str

'''
Iterate the string, expanding the window if the constraints are not satisfied, otherwise contract the window
'''

### Two Pointer Solution
### TC: O(m+n) and SC: O(m+n)
from collections import Counter
class Solution:
    def minWindow(self, s, t):
        if len(t) > len(s): ### corner case
            return ""

        ans = ""
        checkList = Counter(t) ### how many times characters of t need to be contained
        n_check = len(checkList) ### how many constraints are still not finished 

        lp = 0
        for rp in range(len(s)):
            if s[rp] in checkList:
                checkList[s[rp]] -= 1
                if checkList[s[rp]] == 0:
                    n_check -= 1

                while n_check == 0: ### whole t is contained in the window
                    if rp - lp + 1 < len(ans) or ans == "": ### update the min window
                        ans = s[lp:rp+1]
                    if s[lp] in checkList: ### start to contract the window
                        checkList[s[lp]] += 1 ### we are goint to constract the window
                        if checkList[s[lp]] == 1:
                            n_check += 1 ### the constraint is not satisfied now
                    lp += 1
        return ans



