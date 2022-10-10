'''
Leetcode 157. Read N Characters Given Read4

Description:
Given a file and assume that you can only read the file using a given method read4, 
implement a method to read n characters.

Method read4:
The API read4 reads four consecutive characters from file, 
then writes those characters into the buffer array buf4.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.

Method read:
By using the read4 method, implement the method read that reads n characters 
from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.
The return value is the number of actual characters read.

Note:

Consider that you cannot manipulate the file directly. 
The file is only accessible for read4 but not for read.
The read function will only be called once for each test case.
You may assume the destination buffer array, buf, 
is guaranteed to have enough space for storing n characters.
'''

TEXT = "abc"
fp = 0

def read4(buf4):
    global TEXT, fp
    count = 0
    while count < 4:
        if fp < len(TEXT):
            buf4[count] = TEXT[fp]
            fp += 1
            count += 1
        else:
            break
    return count

# @param buf List[str]
# @param n int
# @return int

class Solution:
    def read(self, buf, n):
        count = 0
        buf4 = [''] * 4
        while count < n:
            n_read = read4(buf4)
            for i in range(n_read):
                buf[count] = buf4[i]
                count += 1
                if count == n:
                    break
            if n_read != 4:
                break
        
        return count















