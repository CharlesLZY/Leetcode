'''
Leetcode 394. Decode String

Description:
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].
'''

# @param s str 
# @return str

### Recursion Solution
### TC: O(n) and SC: O(n) where k is the scalar in the pattern k[encoded_string]
class Solution:
    def decodeString(self, s):
        def pairedRightBracket(s): ### trick: important helper function
            count = 0 
            for i in range(len(s)):
                if s[i] == '[':
                    count += 1
                elif s[i] == ']':
                    count -= 1
                    if count == 0:
                        return i

        result = ""
        k = "" ### scalar can have more than one digit
        rightBracket = -1
        for i in range(len(s)):
            if i <= rightBracket:
                continue
            if s[i].isalpha():
                result += s[i]
            elif s[i].isdigit():
                k += s[i]
            elif s[i] == '[':
                rightBracket = i + pairedRightBracket(s[i:])
                result += int(k) * self.decodeString(s[i+1: rightBracket])
                k = ""

        return result

'''
Whenever ']' occurs, pop stack until the first '[', it can be guaranteed that there is no nested brackets
'''
### Stack Solution
### TC: O(n) and SC: O(n)
class Solution:
    def decodeString(self, s):
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else: ### Whenever ']' occurs, pop stack until the first '[', it can be guaranteed that there is no nested brackets 
                temp = ""
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop() ### pop the '['

                ### get k
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                ### the key point of this problem
                stack.append(int(k) * temp) ### push the multiplied string back to the stack

        return ''.join(stack)