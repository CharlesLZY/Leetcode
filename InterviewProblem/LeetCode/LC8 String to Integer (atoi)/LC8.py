'''
Leetcode 8. String to Integer (atoi)

Description:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
'''

# @param s str 
# @return int

### TC: O(n) and SC: O(1)
class Solution:
    def myAtoi(self, s):
        INT_MIN = -pow(2, 31)
        INT_MAX = pow(2, 31) - 1

        result = 0

        sign = 1

        i = 0
        ### skip the leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        ### if there is sign
        if i < len(s) and s[i] == '+':
            sign = 1
            i += 1
        elif i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        ### skip the leading zero
        while i < len(s) and s[i] == '0':
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if sign == 1 else INT_MIN

            result = 10 * result + digit
            i += 1
        
        return sign * result





        