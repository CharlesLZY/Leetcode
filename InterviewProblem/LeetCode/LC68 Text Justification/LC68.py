 '''
Leetcode 68. Text Justification

Description:
Given an array of strings words and a width maxWidth, format the text such that 
each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.
'''

# @param words List[str]
# @param maxWidth int
# @return List[str]

### TC: O(n) and SC: O(n)
class Solution:
    def fullJustify(self, words, maxWidth):
        def curLength(buffer):
            length = 0
            if len(buffer) != 0:
                for word in buffer:
                    length += len(word)
                length += len(buffer) - 1 ### at least one space between words
            return length

        def generateLine(buffer, leftJustified=False):
            n_word = len(buffer)
            if n_word == 1:
                leftJustified = True

            line = ""

            if leftJustified:
                for word in buffer[:len(buffer)-1]:
                    line += word
                    line += ' '
                line += buffer[-1]
                for _ in range(maxWidth - len(line)):
                    line += ' '
                
            else:
                res = maxWidth - curLength(buffer)
                n_space = res // (n_word-1)
                res = res % (n_word-1)
                for word in buffer[:len(buffer)-1]:
                    line += word
                    line += ' '*(n_space+1)
                    if res > 0:
                        line += ' '
                        res -= 1

                line += buffer[-1]
                
            return line

        ans = []
        buffer = []
        for word in words:
            if len(buffer) == 0 or curLength(buffer) + len(word) + 1 <= maxWidth:
                buffer.append(word)
            else:
                ans.append(generateLine(buffer))
                buffer.clear()
                buffer.append(word)

        if buffer:
            ### the last line should be left-justified instead of fully-justified
            ans.append(generateLine(buffer, leftJustified=True)) 

        return ans






