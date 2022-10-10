'''
Leetcode 91. Decode Ways

Description:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into 
letters using the reverse of the mapping above (there may be multiple ways). 
For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
'''

# @param s str 
# @return int

### DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def numDecodings(self, s):
        DP_table = [0]*(len(s)+1) ###  DP[i] : # ways to decode s[:i]
        DP_table[0] = 1 ### for the first DP_table[i-2]

        DP_table[1] = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            if s[i] != '0':
                DP_table[i+1] += DP_table[i]

            if 10 <= int(s[i-1:i+1]) <= 26:
                DP_table[i+1] += DP_table[i-1]

        return DP_table[-1]

### Optimized DP Solution
### TC: O(n) and SC: O(n)
class Solution:
    def numDecodings(self, s):
        prev1 = 1

        prev2 = 0 if s[0] == '0' else 1

        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += prev2

            if 10 <= int(s[i-1:i+1]) <= 26:
                cur += prev1

            prev1, prev2 = prev2, cur

        return prev2


### WRONG SOLUTION
class Solution:
    def isValidBST(self, root):
        if root:
            if root.left:
                if root.left.val >= root.val:
                    return False
            if root.right:
                if root.right.val <= root.val:
                    return False
            '''
            ### Child's right must still be smaller than root
            '''
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return True









