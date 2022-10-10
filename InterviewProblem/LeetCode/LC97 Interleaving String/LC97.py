'''
Leetcode 97. Interleaving String

Description:
An interleaving of two strings s and t is a configuration where s and t are divided into n and m non-empty substrings respectively, such that:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
'''

# @param s1 str
# @param s2 str
# @param s3 str
# @return bool

### Brute Force Solution
### TC: O(2^(m+n)) and SC: O(m+n) ### the size of stack for recursive calls can only go up to m+n
class Solution:
    def isInterleave(self, s1, s2, s3):
        def DFS(i,j):
            nonlocal s1, s2, s3
            if i+j == len(s3):
                return True
            else:
                res = False
                cur = s3[i+j]
                if i < len(s1):
                    if s1[i] == cur:
                        res = res or DFS(i+1,j)
                if j < len(s2):
                    if s2[j] == cur:
                        res = res or DFS(i,j+1)
                return res

        if len(s1) + len(s2) != len(s3): ### corner case
            return False
        
        return DFS(0,0)

### Brute Force Solution (Stack Version)
### TC: O(2^(m+n)) and SC: O(m+n) ### the size of stack for recursive calls can only go up to m+n
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): ### corner case
            return False
        
        stack = [(0,0)]
        while stack:
            i, j = stack.pop()
            if i+j == len(s3):
                return True
            else:
                cur = s3[i+j]
                if i < len(s1):
                    if s1[i] == cur:
                        stack.append((i+1,j))
                if j < len(s2):
                    if s2[j] == cur:
                        stack.append((i,j+1))
        
        return False

### Recursion with memoization
### TC: O(mn) and SC: O(mn)
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): ### corner case
            return False

        DP_table = [[False]*(len(s2)+1) for _ in range(len(s1)+1)] ### do not get the order wrong: len(s2) is inside
        ### DP[i][j] means whether s1[:i] and s2[:j] can form s3[:i+j]
        stack = [(0,0)]
        while stack:
            i, j = stack.pop()
            if i+j == len(s3):
                return True
            else:
                DP_table[i][j] = True

                cur = s3[i+j]
                if i < len(s1):
                    if (s1[i] == cur) and (DP_table[i+1][j] == False):
                        stack.append((i+1,j))
                if j < len(s2):
                    if (s2[j] == cur) and (DP_table[i][j+1] == False):
                        stack.append((i,j+1))
        return False

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): ### corner case
            return False

        DP_table = [[False]*(len(s2)+1) for _ in range(len(s1)+1)] ### do not get the order wrong: len(s2) is inside
        DP_table[0][0] = True ### DP[i][j] means whether s1[:i] and s2[:j] can form s3[:i+j]
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                DP_table[i+1][0] = True
            else:
                break
        for j in range(len(s2)):
            if s2[j] == s3[j]:
                DP_table[0][j+1] = True
            else:
                break
        
        ### DP[1][1] = (DP[0][1] and s1[0]==s3[1]) or (DP[1][0] and s2[0]==s3[1])
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                DP_table[i][j] = (DP_table[i-1][j] and (s1[i-1] == s3[i+j-1])) or (DP_table[i][j-1] and (s2[j-1] == s3[i+j-1]))

        return DP_table[-1][-1]



### Optimized 1D DP Solution
### TC: O(mn) and SC: O(m)
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): ### corner case
            return False

        DP_table = [False]*(len(s1)+1)
        DP_table[0] = True
        for j in range(len(s2)):
            if s2[j] == s3[j]:
                DP_table[j+1] = True
            else:
                break
        
        for i in range(1, len(s1)+1):
            for j in range(len(s2)+1): ### trick: j=0 must be included
                DP_table[i][j] = (DP_table[j] and (s1[i-1] == s3[i+j-1])) or (DP_table[j-1] and (s2[j-1] == s3[i+j-1]))

        return DP_table[-1]
