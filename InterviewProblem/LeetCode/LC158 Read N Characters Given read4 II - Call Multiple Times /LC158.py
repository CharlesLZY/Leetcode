'''
Leetcode 158. Read N Characters Given read4 II - Call Multiple Times

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
Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. 
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
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

'''
这题的trick在于，因为要支持反复调用，但一次必须读4个，所以需要把之前读的存进cache
'''
class Solution:
    def __init__(self):
        self.cache = ['']*4

    def read(self, buf, n):
        count = 0
        if self.cache != ['']*4:
            for i in range(4):
                if self.cache[i] == '':
                    continue
                else:
                    if count < n:
                        buf[count] = self.cache[i]
                        self.cache[i] = ''
                        count += 1
        
        while count < n:
            n_read = read4(self.cache)
            for i in range(n_read):
                buf[count] = self.cache[i]
                self.cache[i] = ''
                count += 1
                if count == n:
                    break
            if n_read != 4:
                break
        
        return count

### Iterator Solution
class Solution:
    def __init__(self):
        self.cache = self.iteration()

    def iteration(self): ### generator is a function return a iterator
        buf4 = ['']*4
        p = 0
        n_read = read4(buf4)
        while n_read != 0:
            yield buf4[p]
            p += 1
            if p == n_read:
                p = 0
                n_read = read4(buf4)

    def read(self, buf, n):
        count = 0
        for i, char in enumerate(self.cache): ### enumerate is just a fancy generator
            buf[i] = char
            count += 1
            if count == n:
                break
        return count













