'''
Leetcode 279. Perfect Squares

Description:
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''

# @param n int 
# @return int


'''
DP[i] = min DP[i - s] + 1 where DP[i] the least number of perfect square numbers that sum to i, s is the square number
         s
'''
### DP Solution (refer to LC322)
### TC: O(n*sqrt(n)) and SC: O(n)
class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        DP_table = [float('inf')] * (n+1)
        DP_table[0] = 0

        for i in range(1, n+1):
            candidates = []
            for s in squares:
                if i - s < 0:
                    break ### squares is ascending
                else:
                    candidates.append(DP_table[i-s])
            DP_table[i] = min(candidates) + 1
        return DP_table[-1] 


'''
Check all depth in ascending order (at most n times)
'''
### Greedy Recursion Solution
class Solution:
    def numSquares(self, n):
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        def DFS(res, count):
            if count == 1:
                return res in squares ### if the residue is a square number, done
            else:
                for s in squares:
                    if DFS(res-s, count-1):
                        return True
                return False

        for count in range(1, n+1): ### trick: at most n square number (all 1s)
            if DFS(n, count):
                return count



### Brute Recursion Solution
class Solution:
    MIN = float("inf")
    def numSquares(self, n):
        self.MIN = float("inf")
        squares = [i**2 for i in range(1, int(n**0.5)+1)]
        def DFS(res, count):
            if res == 0:
                self.MIN = min(self.MIN, count)
                return
            if res < 0:
                return

            for s in squares:
                DFS(res-s, count+1)

        DFS(n, 0)
        return self.MIN