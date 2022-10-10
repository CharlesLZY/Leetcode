'''
Leetcode 166. Fraction to Recurring Decimal

Description:
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Contraints:
- -2^31 <= numerator, denominator <= 2^31 - 1
- denominator != 0

Example:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
'''

# @param numerator int 
# @param denominator int
# @return str

### Hashtable Solution
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: ### corner case: divide by zero
            return 
            
        MAX_INT =  2147483647  ###  2**31 - 1
        MIN_INT = -2147483648  ### -2**31
        if numerator == MIN_INT and denominator == -1: ### corner case: MAX_INT overflow
            return MAX_INT

        if numerator % denominator == 0:
            return str(numerator//denominator)
        else:
            isNegative = (numerator * denominator) < 0
            numerator, denominator = abs(numerator), abs(denominator)
            inter = numerator // denominator
            res = [f"-{inter}." if isNegative else f"{inter}."]

            ### trick: record remainder, if repeated remainder occurs, fractional part will repeat
            hash_table = {} ### remainder: location
            i = 1
            remainder = numerator % denominator
            hash_table[remainder] = i

            remainder *= 10
            while remainder:
                i += 1
                digit = remainder // denominator
                res.append(str(digit))

                remainder = remainder % denominator
                if remainder in hash_table: ### repeating fractional part occurs
                    res.insert(hash_table[remainder], '(')
                    res.append(')')
                    break
                hash_table[remainder] = i
                
                remainder *= 10

            return "".join(res)