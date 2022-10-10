'''
Leetcode 28. Implement strStr()

Description:
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

# @param haystack str
# @param needle str 
# @return int

### Brute Solution
### TC: O(m*n) and SC: O(1)
class Solution:
    def strStr(self, haystack, needle):
        if len(needle) > len(haystack): ### corner case
            return -1
        if needle:
            for i in range(len(haystack) - len(needle) + 1): ### trick
                # if haystack[i:i+len(needle)] == needle:
                #   return i
                for j in range(len(needle)):
                    if haystack[i+j] == needle[j]:
                        if j == len(needle) - 1:
                            return i
                    else:
                        break
                    
            return -1 ### fail to match

        else: ### corner case
            return 0

### KMP solution
### TC: O(m+n) and SC: O(m)
class Solution:
    def strStr(self, haystack, needle):
        def generateNextArray(pattern):
            nextArray = [0] * len(pattern)
            i = 0 ### pointer to backtrack
            j = 1 ### pointer to iterate 
            while j < len(pattern):
                if pattern[j] == pattern[i]:
                    nextArray[j] = i+1
                    i += 1
                    j += 1
                else:
                    if i != 0:
                        i = nextArray[i-1] ### trick: recursive to a sub pattern match problem
                    else:
                        nextArray[j] = i ### i = 0
                        j += 1
            return nextArray


        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        nextArray = generateNextArray(needle)
        i = 0 ### pointer to backtrack pattern
        j = 0 ### pointer to iterate string
        while j < len(haystack):
            if haystack[j] == needle[i]:
                i += 1
                j += 1
                if i == len(needle):
                    return j - i
            else:
                if i != 0:
                    i = nextArray[i-1]
                else:
                    j += 1
        return -1
