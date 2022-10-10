'''
Leetcode 301. Remove Invalid Parentheses

Description:
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.
'''

# @param s str 
# @return List[str]

'''
1. Compute the min number of ')' and '(' to delete
2. Try all possible ways to remove RP and LP (DFS)
3. Remove ')' first to make prefix valid
4. To avoid duplications, when we meed consective duplicated parentheses, only remove the first one and do recursion, then skip the rest
'''

### TC: O(2^(l+r)) and SC: O((1+r)^2)
class Solution:
    ans = []
    def removeInvalidParentheses(self, s):
        self.ans = []
        def isValid(string):
            
            count = 0 ### number of unpaired '('
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    if count == 0:
                        return False
                    else:
                        count -= 1
                else:
                    continue
            return True

        def DFS(string, start, n_LP, n_RP): ### the key point: start index (without it, there will be a lot of duplicated outcomes)
            if n_LP == 0 and n_RP == 0 and isValid(string):
                self.ans.append(string)
                return
            else:
                
                if n_RP != 0: ### trick 1: delete invalid parentheses first (branch pruning), if the n_RP != 0, the prefix is always invalid
                    i = start
                    while i < len(string):
                        if string[i] == ')': ### we take the first ')' we meet for recursion
                            DFS(string[:i]+string[i+1:], i, n_LP, n_RP-1) ### the start index is important, it will eliminate tons of wrong branches
                            ### trick 2: when encounter consective same parentheses, we only use the first one to DFS and skip the others
                            while i+1 < len(string) and string[i+1] == ')': ### to avoid consective ')' causing duplicated branches
                                 i += 1
                        i += 1
                else: ### only when all invalid RP are removed, we begin to remove invalid LP and very importantly, start from the position of the last RP deleted
                    i = start
                    while i < len(string):
                        if string[i] == '(': ### we take the first '(' we meet for recursion
                            DFS(string[:i]+string[i+1:], i, n_LP-1, n_RP) ### the start index is important, it will eliminate tons of wrong branches
                            ### trick 2: when encounter consective same parentheses, we only use the first one to DFS and skip the others
                            while i+1 < len(string) and string[i+1] == '(':  ### to avoid consective '(' causing duplicated branches
                                 i += 1
                        i += 1

        ### count how many invalid parentheses need to delete
        count = 0
        n_LP = 0  ### number of invalid left parentheses to delete
        n_RP = 0  ### number of invalid right parentheses to delete
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    n_RP += 1
                else:
                    count -= 1
            else:
                continue
        n_LP = count ### the remained left parentheses are invalid

        DFS(s, 0, n_LP, n_RP)
        return self.ans

