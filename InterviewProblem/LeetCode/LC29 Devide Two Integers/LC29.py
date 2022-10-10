'''
Leetcode 29. Divide Two Integers

Description:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor
'''

# @param dividend int 
# @param divisor int 
# @return int

### Intuitive Substraction Solution
### TC: O(n) and SC: O(1)
class Solution:
    def divide(self, dividend, divisor): ### implement a // b
        MAX_INT =  2147483647  ###  2**31 - 1
        MIN_INT = -2147483648  ### -2**31

        if dividend == MIN_INT and divisor == -1: ### corner case: MAX_INT overflow
            return MAX_INT

        sign = (dividend > 0)^(divisor > 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend > divisor:
            quotient += 1
            dividend -= divisor

        return -quotient if sign else quotient


### Optimized Substraction Solution
### TC: O(logn) and SC: O(1)
class Solution:
    def divide(self, dividend, divisor): ### implement a // b
        MAX_INT =  2147483647  ###  2**31 - 1
        MIN_INT = -2147483648  ### -2**31

        if dividend == MIN_INT and divisor == -1: ### corner case: MAX_INT overflow
            return MAX_INT

        sign = (dividend > 0)^(divisor > 0) ### xor
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            res = 1
            temp = divisor
            while dividend >= temp:
                dividend -= temp
                quotient += res
                res = res << 1
                temp = temp << 1

        return -quotient if sign else quotient 

### another version
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT =  2147483647  ###  2**31 - 1
        MIN_INT = -2147483648  ### -2**31

        if dividend == MIN_INT and divisor == -1: ### corner case: MAX_INT overflow
            return MAX_INT
        sign = (dividend > 0) ^ (divisor > 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            res = 1 ### quotient
            div = divisor
            temp = dividend - div
            while temp >= div:
                div = div << 1
                res = res << 1
                temp = dividend - div
            quotient += res
            dividend -= div
        return -quotient if sign else quotient 


