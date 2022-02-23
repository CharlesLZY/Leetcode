'''
Leetcode 1871. Jump Game VII

Description:
You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. 
You can move from index i to index j if the following conditions are fulfilled:
- i + minJump <= j <= min(i + maxJump, s.length - 1) 
- s[j] == '0' 
Return true if you can reach index s.length - 1 in s, or false otherwise.
'''

'''
有最小最大步数限制且只有在0的位置可以跳
'''

# @param s str 
# @param minJump int 
# @param maxJump int 
# @return bool

### BFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def canReach(self, s, minJump, maxJump):
        if s[-1] == "1": ### corner case
            return False 
        queue = [0]
        curFar = 0 ### current furthest
        while queue:
            idx = queue.pop(0)
            if idx == len(s)-1:
                return True
            # low = idx + minJump ### can be optimized
            low = max(curFar+1, idx + minJump) ### at least go further one step
            high = min(len(s)-1, idx + maxJump)
            for jump in range(low, high+1):
                if s[jump] == '0':
                    queue.append(jump)
            curFar = idx+maxJump
        return False

### DFS Solution
### TC: O(n) and SC: O(n)
class Solution:
    def canReach(self, s, minJump, maxJump):
        def DFS(idx):
            if idx < 0 or idx >= len(s) or s[idx] != '0':
                return False
            if idx == len(s)-1:
                return True
            for jump in range(minJump, maxJump+1):
                if DFS(idx+jump):
                    return True
            return False
        if s[-1] == "1": ### corner case
            return False 
        return DFS(0)


'''
DP[i] means whether we can reach the last index starting from index i

DP[i] = True if there is a True from i+minJump to i+maxJump
0 x x x i x x x x i+minJump x x x x i+maxJump x x x x 0
'''

### DP Solution 看不懂啊，这什么神仙解法
### TC: O(nk) and SC: O(n) where k = maxJump - minJump
class Solution:
    def canReach(self, s, minJump, maxJump):
        if s[-1] == "1": ### corner case
            return False 

        DP_table = [False] * n
        DP_table[-1] = True ### set for the index len(s) - 1

        tc = 0 #number of Trues between i+minJum, i+maxJump
        for i in range(n-2, -1, -1):
            if s[i] == "1": 
                continue 
            if i+1+maxJump < len(s) and DP_table[i+1+maxJump] == True: 
                tc -= 1
            if i+minJump < len(s) and DP_table[i+minJump] == True: 
                tc += 1
            DP_table[i] = tc >= 1  

        return DP_table[0]