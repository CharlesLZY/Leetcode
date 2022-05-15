'''
Leetcode 5. Longest Palindromic Substring

Description:
Given a string s, return the longest palindromic substring in s.
'''

# @param s str 
# @return str

'''
DP[i][j] whether s[i:j+1] is palindrome
DP[i][j] = DP[i+1][j-1] and s[i] == s[j]
Base cases: DP[i][i] = True, DP[i][i+1] = s[i] == s[i+1]
'''


### Brute Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def longestPalindrome(self, s):
        def checkPalindrome(s):
            return s == s[::-1]
        res = ""
        for i in range(len(s)): 
            if i+1 < len(s) and s[i] == s[i+1]: ### .. b a a b ..
                r = 0 ### radius
                while i-r >= 0 and i+r+2 <= len(s) and checkPalindrome(s[i-r:i+r+2]):
                    if len(s[i-r:i+r+2]) > len(res):
                        res = s[i-r:i+r+2]
                    r += 1
            ### .. b a b ..
            r = 0 ### radius
            while i-r >= 0 and i+r+1 <= len(s) and checkPalindrome(s[i-r:i+r+1]):
                if len(s[i-r:i+r+1]) > len(res):
                    res = s[i-r:i+r+1]
                r += 1

        return res

### Center Extending Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def longestPalindrome(self, s):
        def checkPalindrome(s):
            return s == s[::-1]
        res = ""
        r = 0 ### shared radius, the longest substring must beat the former one
        for i in range(len(s)): ### .. b a a b ..
            while i-r >= 0 and i+r+2 <= len(s) and checkPalindrome(s[i-r:i+r+2]):
                if s[i-r] == s[i+r+1]:
                    if 2*r+2 > len(res):
                        res = s[i-r:i+r+2]
                    r += 1
                else:
                    break

        for i in range(len(s)): ### .. b a b ..
            while i-r >= 0 and i+r+1 <= len(s) and checkPalindrome(s[i-r:i+r+1]):
                if s[i-r] == s[i+r]:
                    if 2*r+1 > len(res):
                        res = s[i-r:i+r+1]
                    r += 1
                else:
                    break

        return res

class Solution:
    def longestPalindrome(self, s):
        MAX = s[0]
        for i in range(len(s)-1):
            ### ...abba...
            if s[i+1] == s[i]:
                lp = i
                rp = i+1
                while lp >= 0 and rp < len(s):
                    if s[lp] == s[rp]:
                        if rp-lp+1 > len(MAX):
                            MAX = s[lp:rp+1]
                        lp -= 1
                        rp += 1
                    else:
                        break
            ### ...aba...
            lp = i-1
            rp = i+1
            while lp >= 0 and rp < len(s):
                if s[lp] == s[rp]:
                    if rp-lp+1 > len(MAX):
                        MAX = s[lp:rp+1]
                    lp -= 1
                    rp += 1
                else:
                    break
        return MAX


### DP Solution
### TC: O(n^2) and SC: O(n^2)
class Solution:
    def longestPalindrome(self, s):
        DP_table = [[None for i in range(len(s))] for _ in range(len(s))] ### DP[i][j] means whether s[i:j] is palindrome
        max_length = 1
        index = 0
        for i in range(len(s)): ### for single char
            DP_table[i][i] = True
        for i in range(len(s)-1):
            DP_table[i][i+1] = s[i]==s[i+1] ### AA type
            if s[i]==s[i+1]:
                max_length = 2
                index = i


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

        ### filling the DP table along the diagonal
        for i in range(len(s)-2):
            for j in range(len(s)-2-i):
                DP_table[j][j+2+i] = DP_table[j+1][j+1+i] and s[j]==s[j+2+i]
                if DP_table[j][j+2+i] and i+3 > max_length:
                    max_length = i+3
                    index = j

        return s[index:index+max_length]


### Another Version
class Solution:
    def longestPalindrome(self, s):
        DP_table = [[None for i in range(len(s))] for _ in range(len(s))] ### DP[i][j] means whether s[i:j] is palindrome
        max_length = 1
        index = 0
        for i in range(len(s)): ### for single char
            DP_table[i][i] = True
        for i in range(len(s)-1):
            DP_table[i][i+1] = s[i]==s[i+1] ### AA type
            if s[i]==s[i+1]:
                max_length = 2
                index = i


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

        ### filling the DP table along the diagonal
        for i in range(len(s)-2, -1, -1): ### trick: must be in reverse order (因为会用到下面一行的信息)
            for j in range(2+i, len(s)):
               
                DP_table[i][j] = DP_table[i+1][j-1] and s[i]==s[j] ### use the information of row i+1, so we need to update DP table from bottom to top
                
                if DP_table[i][j] and j-i+1 > max_length:
                    max_length = j-i+1
                    index = i
        
        return s[index:index+max_length]