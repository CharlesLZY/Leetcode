'''
Leetcode 1087. Brace Expansion

Description:
You are given a string s representing a list of words. Each letter in the word has one or more options.

If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options. For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, if s = "a{b,c}", the first character is always 'a', but the second character can be 'b' or 'c'. The original list is ["ab", "ac"].

Return all words that can be formed in this manner, sorted in lexicographical order.
'''

# @param s str 
# @return List[str]

### Intuitive Backtrack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def expand(self, s):
        res = []
        letters = [] ### List[List[char]]
        i = 0
        while i < len(s):
            if s[i] == '{':
                i += 1
                letters.append([])
                while s[i] != '}':
                    if s[i] != ',':
                        letters[-1].append(s[i])
                    i += 1
            elif s[i] == '}':
                i += 1
            else:
                letters.append([s[i]])
                i += 1

        def forward(string, depth):
            if depth == len(letters):
                res.append(string)
                return
            else:
                for char in letters[depth]:
                    forward(string+char, depth+1)

        forward("", 0)
        res.sort()
        return res

### Faster Solution
### TC: O(n) and SC: O(n)
class Solution:
    def expand(self, s):
        letters = [] ### List[List[char]]
        i = 0
        while i < len(s):
            if s[i] == '{':
                i += 1
                letters.append([])
                while s[i] != '}':
                    if s[i] != ',':
                        letters[-1].append(s[i])
                    i += 1
            elif s[i] == '}':
                i += 1
            else:
                letters.append([s[i]])
                i += 1

        res = []
        if letters:
            res = letters.pop(0)
        for chars in letters:
            res = [string + char for string in res for char in chars]


        res.sort()
        return res