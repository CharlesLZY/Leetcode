'''
Leetcode 69. Sqrt(x)

Description:
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
'''

# @param x int 
# @return int

### Divide and Conquer (因为这题return的是个int)
### TC: O(logn) and SC: O(1)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        lp = 2
        rp = x // 2
        while lp <= rp:
            mid = (lp + rp) // 2
            square = mid * mid
            if square > x:
                rp = mid - 1
            elif square < x:
                lp = mid + 1
            else:
                return mid
        return rp


'''
sqrt(n) = x, we want to find the solution of f(x) = x^2 - n = 0
Use Taylor expansion: f(x) = f(x_0) + f'(x_0)(x-x_0) + ...
f(x_0) + f'(x_0)(x-x_0) = 0
x_1 = x_0 - f(x_0)/f'(x_0)
...
x_n+1 = x_n - f(x_n)/f'(x_n)

'''
### Newton's Method
### TC: O(logn) and SC: O(1)
class Solution:
    def mySqrt(self, x):
        def f(z):  ### f(z) = z^2 - x
            return z*z - x

        def df(z): ### derivate of f(z) = z^2 - x
            return 2*z

        threshold = 1e-5

        x_n = x // 2
        while abs(f(x_n)) > threshold:
            x_n = x_n - f(x_n) / df(x_n)

        return x_n


### Gradient Descent
class Solution:
    def mySqrt(self, x):  
        def f(z):  ### f(z) = (z^2 - x)^2
            return (z*z - x) * (z*z - x)
        def df(z): ### derivate of f(z) = (z^2 - x)^2
            return 4*z*z*z - 2*x*2*z

        threshold = 1e-5
        alpha = 0.001
        x_n = x // 2
        while abs(f(x_n)) > threshold:
            x_n = x_n - alpha * df(x_n)
            print(x_n)
        return x_n


### x^(1/n) = exp(ln(x)/n) then do the Taylor expansion