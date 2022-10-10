'''
Leetcode 1307. Verbal Arithmetic Puzzle

Description:
Given an equation, represented by words on the left side and the result on the right side.

You need to check if the equation is solvable under the following rules:
- Each character is decoded as one digit (0 - 9).
- No two characters can map to the same digit.
- Each words[i] and result are decoded as one number without leading zeros.
- Sum of numbers on the left side (words) will equal to the number on the right side (result).

Return true if the equation is solvable, otherwise return false.

Constraints:
- 2 <= words.length <= 5
- 1 <= words[i].length, result.length <= 7
- words[i], result contain only uppercase English letters.
- The number of different characters used in the expression is at most 10.

Example:
Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
'''

# @param words List[str]
# @param result str 
# @return bool

### TC: O(n) and SC: O(n)
class Solution:
    def isSolvable(self, words, result):
        ### simulate vertical calculation
        words.append(result) ### trick: words[-1] is result and it will be treated as negative. sum(words) should be 0
        R, C = len(words), max(map(len, words))
        assigned = {}
        assigned_inv = [None] * 10 ### trick: in this problem, there are at most 10 different characters
        
        ### fix the column then row by row
        def forward(col, row, res):
            nonlocal R, C
            ### termination condition
            if col == C: ### all digits have been calculated
                return res == 0
            
            if row == R: ### all words have been calculated in this column
                return res % 10 == 0 and forward(col+1, 0, res // 10) ### move to the next column
                
            cur_word = words[row]
            if col >= len(cur_word):
                return forward(col, row+1, res) ### move to the next word
            
            cur_char = cur_word[~col] ### trick: ~_ can help to index the string in reverse order
            sign = -1 if row == R - 1 else 1 ### trick: treat the last word(result) as negative
            if cur_char in assigned:
                if assigned[cur_char] == 0 and len(cur_word) != 1 and col == len(cur_word)-1: ### leading zero
                    return False ### this value assignment is invalid
                else:
                    return forward(col, row+1, res + sign * assigned[cur_char])
            else:
                for digit, char in enumerate(assigned_inv):
                    if char is None and not (digit == 0 and len(cur_word) != 1 and col == len(cur_word)-1):
                        assigned_inv[digit] = cur_char
                        assigned[cur_char] = digit
                        if forward(col, row+1, res + sign * assigned[cur_char]):
                            return True
                        ### backtrack
                        assigned_inv[digit] = None
                        del assigned[cur_char]
                return False
        
        return forward(0,0,0)