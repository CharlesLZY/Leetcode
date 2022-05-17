'''
Leetcode 43. Multiply Strings

Description:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

# @param num1 str
# @param num2 str
# @return str

'''
     1 2 3
   x 4 5 6
____________
     7 3 8
   6 1 5 0
 4 9 2 0 0
____________
 5 7 0 8 8

'''

### Simulate the arithmetic
### TC: O(mn) and SC: O(m+n)
class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0": ### corner case
            return "0"

        def val(i):
            return ord(i)-ord('0')

        num1 = num1[::-1] ### reverse the string for convenience
        num2 = num2[::-1] ### reverse the string for convenience

        def multiplyOneDigit(num, digit): ### num is reversed
            ans = [] ### digits of the result in reversed order
            carry = 0
            for n in num:
                temp = val(n) * val(digit) + carry
                carry = temp // 10
                ans.append(temp % 10)
            if carry > 0:
                ans.append(carry)
            return ans

        numToSum = []

        for i in range(len(num2)):
            ### trick: 123 * 200 = 123*100 * 2
            numToSum.append(multiplyOneDigit('0'*i+num1, num2[i])) ### nums has been reversed

        result = numToSum.pop() ### initialize the answer
        
        for num in numToSum:
            res = []
            carry = 0 ### must put here
            for digit1, digit2 in zip_longest(num, result, fillvalue=0): ### if len(res) != len(num), then padding 0
                temp = digit1 + digit2 + carry
                carry = temp // 10
                res.append(temp % 10)

            if carry > 0:
                res.append(carry)

            result = res
        result.reverse()
        return ''.join(str(digit) for digit in result)










