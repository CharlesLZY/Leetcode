'''
Leetcode 40. Combination Sum II

Description:
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

'''
Must all positive, if there is negative number and the same number can be use for any times, this problem can not be solved.
'''

# @param candidates List[int]
# @param target int
# @return List[List[int]]

### 这题的难点在于不能有重复解

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def DFS(path, res, idx):
            if res == 0:
                ans.append(path[:])
                return
            while idx < len(candidates):
                
                if res - candidates[idx] >= 0:
                    path.append(candidates[idx])
                    DFS(path, res-candidates[idx], idx+1)
                    path.pop()
                else:
                    break
                
                ### skip the following duplicate
                ### avoid use this number in this location (不在这一位用这个数了)
                while idx < len(candidates)-1 and candidates[idx] == candidates[idx+1]:
                    idx += 1
                idx += 1

        DFS([], target, 0)
        return ans

### another version
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def DFS(path, res, start):
            if res == 0:
                ans.append(path[:])
                return
            idx = start
            for i in range(start, len(candidates)):
                
                ### skip the duplicate
                if i > start and candidates[i] == candidates[i-1]:
                    i += 1
                    continue

                if res - candidates[i] >= 0:
                    path.append(candidates[i])
                    DFS(path, res-candidates[i], i+1)
                    path.pop()
                else:
                    break

        DFS([], target, 0)
        return ans


