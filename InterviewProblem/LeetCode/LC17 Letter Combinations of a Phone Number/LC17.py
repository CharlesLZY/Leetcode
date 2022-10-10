'''
Leetcode 17. Letter Combinations of a Phone Number

Description:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
'''

# @param digits str 
# @return List[str]

class Solution:
    def letterCombinations(self, digits):
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        ans = []
        def DFS(path, depth):
            if depth == len(digits):
                ans.append(''.join(path))
                return
            cur = digits[depth]
            for char in letters[cur]:
                path[depth] = char
                DFS(path, depth+1)

        if digits: ### corner case
            DFS([None for _ in range(len(digits))], 0)

        return ans