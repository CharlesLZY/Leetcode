'''
Leetcode 65. Valid Number

Description:
A valid number can be split up into these components (in order):
- A decimal number or an integer.
- (Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One of the following formats:
    - One or more digits, followed by a dot '.'.
    - One or more digits, followed by a dot '.', followed by one or more digits.
    - A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
Given a string s, return true if s is a valid number.
'''

# @param s str 
# @return bool

### TC: O(n) and SC: O(1)
class Solution:
    def isNumber(self, s):
        sign = ['-', '+']
        num = [str(n) for n in range(10)]
        dot = '.'
        e = ['e', 'E']

        def checkInteger(substring):
            if len(substring) == 0:
                return False

            if substring[0] in sign:
                substring = substring[1:]

            if len(substring) == 0:
                return False

            for digit in substring:
                if digit not in num:
                    return False

            return True

        def checkNumber(substring):
            if len(substring) == 0:
                return False

            if substring[0] in sign:
                substring = substring[1:]

            if len(substring) == 0:
                return False

            dotFound = False
            i = 0
            while i < len(substring):
                if substring[i] == dot:
                    if dotFound or len(substring) == 1:
                        return False
                    else:
                        dotFound = True
                else:
                    if substring[i] not in num:
                        return False
                
                i += 1

            return True

        eFound = -1
        for i, char in enumerate(s):
            if char in e:
                if eFound == -1:
                    eFound = i
                else:
                    return False

        if eFound != -1:
            return checkNumber(s[:eFound]) and checkInteger(s[eFound+1:])
        else:
            return checkNumber(s)


### Deterministic Finite Automaton(DFA) Solution
class Solution(object):
    def isNumber(self, s):
        ### 可以用这个把DFA画出来
        DFA = [
            {"digit": 1, "sign": 2, "dot": 3},     ### state 0
            {"digit": 1, "dot": 4, "exponent": 5}, ### state 1
            {"digit": 1, "dot": 3},                ### state 2
            {"digit": 4},                          ### state 3
            {"digit": 4, "exponent": 5},           ### state 4
            {"sign": 6, "digit": 7},               ### state 5
            {"digit": 7},                          ### state 6
            {"digit": 7}                           ### state 7
        ]
        
        current_state = 0
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]:
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in DFA[current_state]:
                return False
            
            current_state = DFA[current_state][group]
        
        return current_state in [1, 4, 7]








