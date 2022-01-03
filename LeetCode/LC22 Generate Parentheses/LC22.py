'''
Leetcode 22. Generate Parentheses

Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

# @param n int
# @return List[str]

class Solution:
    def generateParenthesis(self, n):
        ans = []
        def forward(path, n_lp, n_rp):
            if n_lp == n and n_rp == n:
                ans.append(''.join(path))
                return
            if n_lp < n:
                path[n_lp+n_rp] = '('
                forward(path, n_lp+1, n_rp)
            if n_rp < n_lp:
                path[n_lp+n_rp] = ')'
                forward(path, n_lp, n_rp+1)
        forward([None for _ in range(2*n)], 0, 0)
        return ans

