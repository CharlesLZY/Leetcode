'''
Leetcode 204. Count Primes

Description:
Given an integer n, return the number of prime numbers that are strictly less than n.
'''

# @param n int
# @return int

### Brute Solution
class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        count = 0
        for p in range(2, n):
            flag = 0
            for div in range(2, p):
                if p % div == 0:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        return count

### Optimized Solution
class Solution:
    def countPrimes(self, n):
        primes = [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1): ### trick: to save time complexity
            if primes[p]:
                # for multiple in range(p * 2, n, p): ### set all multiples of p to False
                for multiple in range(p * p, n, p): ### can start from p*p because p * k where k < p has been checked
                    primes[multiple] = False
        
        return sum(primes) ### the remaining true is primes