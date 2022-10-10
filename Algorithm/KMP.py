'''
KMP algorithm for pattern searching
一个人能走多远不在于他在顺境的时候能走多快，而在于他在逆境的时候多久能找到曾经的自己。

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

Naive solution: each time fail to match pattern need to backtrack the pointer on the string
KMP: only need to backtrack the pointer on the pattern. The key is to find the common prefix and postfix.

一句话概括: string的指针永远前进，失败匹配时，将pattern的指针回溯到最远公共前后缀的位置（前缀的后一个位置），使得公共前缀来到公共后缀的位置
移动完成之后，pattern指针左边子串的长度就是公共前后缀的长度

          X
A B B A B C A B B A B D

A B B A B D
          X
->
          X
A B B A B C A B B A B D

      A B B A B D
          X
->
          X
A B B A B C A B B A B D

          A B B A B D
          X
->
            X
A B B A B C A B B A B D

            A B B A B D
            X

通过建立next数组，来标记pattern的子串的最长公共前后缀的位置
A B C A C
0 0 0 1 0

A B A B A A A B A B A A
0 0 1 2 3 1 1 2 3 4 5 6


生成next数组的过程和利用next数组去匹配pattern的过程几乎一致，原因在于生成next数组的过程其实也是一个匹配pattern的过程
这时的pattern是当前的common prefix和postfix

i j                             i   j                            i   j  
A B A B A A A B A B A A   ->    A B A B A A A B A B A A   ->   A B A B A A A B A B A A  ->
0 0                             0 0 1                          0 0 1 2

    i   j                             i   j             
A B A B A A A B A B A A   ->    A B A B A A A B A B A A 
0 0 1 2 3                       0 0 1 2 3 

这个时候其实相当于转化成这样一个pattern匹配问题
               j
string:  A B A A A B A B A A 
pattern: A B A B (目前的common prefix，它的next是已经计算过了的)
               i
nextArr: 0 0 1 2
当 pattern【j] != pattern[i], i = nextArray[i-1] 就相当于平移到prefix(pattern的)的prefix位置去
               j
string:  A B A A A B A B A A 
pattern:     A B A B
               i
nextArr:     0 0 1 2

               j
string:  A B A A A B A B A A 
pattern:       A B A B
               i
nextArr:       0 0 1 2

i         j                      i         j                    i           j
A B A B A A A B A B A A   ->   A B A B A A A B A B A A   ->   A B A B A A A B A B A A  ->
0 0 1 2 3 1                    0 0 1 2 3 1 1                  0 0 1 2 3 1 1 2 

    i           j                    i           j                    i           j                  i           j
A B A B A A A B A B A A   ->   A B A B A A A B A B A A   ->   A B A B A A A B A B A A  ->  A B A B A A A B A B A A
0 0 1 2 3 1 1 2 3              0 0 1 2 3 1 1 2 3 4            0 0 1 2 3 1 1 2 3 4 5        0 0 1 2 3 1 1 2 3 4 5 6
'''

### Find the pattern first occur in the string
### TC: O(n) and SC: O(m)
def patternSearch(string, pattern):
    def generateNextArray():
        nextArray = [0] * len(pattern)
        i = 0 ### backtrack pointer for pattern
        j = 1 ### start from the second number
        while j < len(pattern):
            if pattern[j] == pattern[i]:
                nextArray[j] = i + 1
                i += 1
                j += 1
            else:
                if i != 0:
                    i = nextArray[i-1] ### trick
                else:
                    nextArray[j] = i ### i = 0
                    j += 1

        return nextArray

    nextArray = nextArray()
    
    if len(pattern) == 0:
        return 0
    if len(string) < len(pattern):
        return -1
    i = 0 ### pointer on string
    j = 0 ### pointer on pattern
    while (i < len(string)):
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = nextArray[j-1] ### trick
            else:
                i += 1
    return -1

### Find all patterns in the string
### 如果要找到所有的出现位置，这时候不可避免的需要在string中回溯，比如极端case: string: AAAAAAAA and pattern: AAAAA