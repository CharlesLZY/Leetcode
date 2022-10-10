'''
Leetcode 647. Palindromic Substrings

Description:
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
'''

# @param s str 
# @return int

### Brute Solution
### TC: OL(n^3) and SC: O(1)
class Solution:
    def countSubstrings(self, s):
        def checkPalindrome(s):
            # for i in range(len(s) // 2):
            #     if s[i] != s[len(s)-1-i]:
            #         return False
            # return True
            return s == s[::-1]

        res = 0
        for size in range(1, len(s)+1):
            for lp in range(len(s)-size+1):
                if checkPalindrome(s[lp:lp+size]):
                    res += 1

        return res

### Center Extending Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def countSubstrings(self, s):
        def checkPalindrome(s):
            return s == s[::-1]
        ans = 0
        for i in range(len(s)): ### .. b a a b ..
            r = 0
            while i-r >= 0 and i+r+2 <= len(s):
                if s[i-r] == s[i+r+1]:
                    ans += 1
                    r += 1
                else:
                    break

        for i in range(len(s)): ### .. b a b ..
            r = 0
            while i-r >= 0 and i+r+1 <= len(s):
                if s[i-r] == s[i+r]:
                    ans += 1
                    r += 1
                else:
                    break

        return ans

### DP Solution
### TC: O(n^2) and SC: O(n^2)
class Solution:
    def countSubstrings(self, s):
        ans = 0
        DP_table = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            DP_table[i][i] = True
            ans += 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                DP_table[i][i+1] = True
                ans += 1

        '''
            a b c b a a b
            0 1 2 3 4 5 6 
        0   T F
        1     T F
        2       T F
        3         T F
        4           T T
        5             T F
        6               T

        '''
        ### just filling the DP table along the diagonal
        for i in range(len(s)-2):
            for j in range(len(s)-2-i):
                DP_table[j][j+2+i] = DP_table[j+1][j+1+i] and s[j]==s[j+2+i]
                if DP_table[j][j+2+i]:
                    ans += 1

        for kernel_size in range(1, len(s)-1):
            for lp in range(len(s) - kernel_size - 1):
                


        return ans