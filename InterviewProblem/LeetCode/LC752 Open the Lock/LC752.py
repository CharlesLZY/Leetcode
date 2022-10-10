'''
Leetcode 752. Open the Lock

Description:
You have a lock in front of you with 4 circular wheels. 
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''

# @param deadends List[str]
# @param target str
# @return int

from collections import deque
class Solution:
    def openLock(self, deadends, target):
        if '0000' in deadends: ### corner case
            return -1
        
        visited = set(deadends)
        queue = deque([('0000', 0)])
        visited.add('0000')
        while queue:
            cur, cur_depth = queue.popleft()
            if cur == target:
                return cur_depth
            for i in range(4):
                digit = int(cur[i])
                up = cur[:i]+ str((digit+1) % 10) +cur[i+1:]
                if up not in visited:
                    visited.add(up) ### trick: must mark it as visited here to avoid infinite loop
                    queue.append((up, cur_depth+1))
                down = cur[:i]+ str((digit-1) % 10) +cur[i+1:]
                if down not in visited:
                    visited.add(down) ### trick: must mark it as visited here to avoid infinite loop
                    queue.append((down, cur_depth+1))
        
        return -1