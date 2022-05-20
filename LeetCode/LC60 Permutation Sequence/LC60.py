'''
Leetcode 60. Permutation Sequence

Description:
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence.
'''

# @param n int
# @param k int
# @return str

### Basic Solution
class Solution:
    def getPermutation(self, n, k):
        self.count = 0
        self.ans = None
        def DFS(path, candidates):
            if self.count == k:
                return 
            if len(candidates) == 0:
                self.count += 1
                if self.count == k:
                    self.ans = "".join([str(i) for i in path])

            else:
                for i in range(len(candidates)):
                    path.append(candidates[i])
                    DFS(path, candidates[:i]+candidates[i+1:])
                    path.pop()

        DFS([], [i for i in range(1,n+1)])
        return self.ans


'''
N! - 1 = sum_{k=0}^{N-1} k*k!
Proof:
(N+1)! - N! =  N*N!
N! - (N-1)! = (N-1)*(N-1)!

1 2 3 => 0*0! + 0*1! + 0*2!
...
2! -     1! = 1*1!    

We can use factorial number system to map all permutations from
k = 0 = sum_{k=0}^{N-1} 0*k!
k = N!-1 = sum_{k=0}^{N-1} k*k!


'''
### Factorial Number System
### TC: O(n) and SC: O(1)
class Solution:
    def getPermutation(self, n, k):
        nums = [i for i in range(1, n+1)]
        factorials = [1]
        for i in range(1, n):
            factorials.append(factorials[i-1]*i) ### factorial[i] = i!


        k = k-1 ### mapping from 0 to N!-1
        output = []
        for i in range(n - 1, -1, -1):
            ### trick: greedy
            ### 为什么可以用这种方式找映射？因为N!= sum_{k=0}^{N-1} k*k! + 1 > sum_{k=0}^{N-1} k*k!
            idx = k // factorials[i]
            k -= idx * factorials[i]
            
            output.append(nums[idx])
            del nums[idx]
        
        return ''.join(output)











        