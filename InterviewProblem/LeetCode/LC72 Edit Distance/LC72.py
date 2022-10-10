'''
Leetcode 72. Edit Distance

Description:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character
'''

# @param word1 str 
# @param word2 str 
# @return int

### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        ### start from the empty string
        DP_table = [[0]*(n+1) for _ in range(m+1)] ### DP[i][j]: the edit distance between word1[:i] and word2[:j]
        '''
        It turns out that one could compute D[i][j], knowing D[i - 1][j], D[i][j - 1] and D[i - 1][j - 1].
        If word1[i] == word2[j]:
        DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1])  
        else:
        DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1]+1)
        '''

        for i in range(m+1): ### word2 is empty, so the distance is i
            DP_table[i][0] = i
            
        for i in range(n+1): ### word1 is empty, so the distance is i
            DP_table[0][i] = i

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    DP_table[i][j] = min(DP_table[i-1][j]+1, DP_table[i][j-1]+1, DP_table[i-1][j-1])
                else:
                    DP_table[i][j] = min(DP_table[i-1][j]+1, DP_table[i][j-1]+1, DP_table[i-1][j-1]+1)

        return DP_table[m][n]