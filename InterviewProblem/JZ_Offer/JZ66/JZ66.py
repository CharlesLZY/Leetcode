'''
JZ66 构建乘积数组

描述：
给定一个数组 A[0,1,...,n-1] ,请构建一个数组 B[0,1,...,n-1], 其中 B 的元素 B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
（除 A[i] 以外的全部元素的的乘积）。程序中不能使用除法。
（注意：规定 B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2]）
对于 A 长度为 1 的情况，B 无意义，故而无法构建，用例中不包括这种情况。
'''

# @param A List[int] 
# @return List[int]


'''
B[i] = A[0]*A[1]*...*A[i-1] * A[i+1]*...*A[n-1] = left[i] * right[i]
'''
### TC: O(n) and SC: O(n)
class Solution:
    def multiply(self, A):
        left  = [1]*len(A)
        right = [1]*len(A)
        for i in range(1, len(A)):
            left[i] = left[i-1]*A[i-1]
            right[len(A)-1-i] = right[len(A)-i]*A[len(A)-i]
        B = []
        for i in range(len(A)):
            B.append(left[i]*right[i])
        return B


'''
B[i] = A[0]*A[1]*...*A[i-1] * A[i+1]*...*A[n-1] = left[i] * right[i]
We can use array B as left/right array temporarily and track right[i]/left[i] each time, to solve the problem without extra space complexity
'''
### TC: O(n) and SC: O(1)
class Solution:
    def multiply(self, A):
        B  = [1]*len(A) ### no use of extra space complexity, B is what we want to reture
        for i in range(1, len(A)):
            B[i] = B[i-1]*A[i-1] ### left array
        rp = 1
        for i in range(len(A)-2, -1, -1):
            rp *= A[i+1] ### update right[i]
            B[i] *= rp ### B[i] is left[i]
        return B

### TC: O(n) and SC: O(1)
class Solution:
    def multiply(self, A):
        B  = [1]*len(A) ### no use of extra space complexity, B is what we want to reture
        for i in range(len(A)-2, -1, -1):
            B[i] = B[i+1]*A[i+1] ### right array
        lp = 1
        for i in range(1, len(A)):
            lp *= A[i-1] ### update left[i]
            B[i] *= lp ### B[i] is right[i]
        return B
