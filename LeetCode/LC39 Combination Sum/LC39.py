'''
Leetcode 39. Combination Sum

Description:
Given an array of distinct positive integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
Must all positive, if there is negative number and the same number can be use for any times, this problem can not be solved.
'''

# @param candidates List[int] 
# @param target int 
# @return List[List[int]]


class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        # candidates.sort() ### important: sort all numbers and incrementally build the combination
        def DFS(res, path, idx):
            if res == 0:
                ans.append(path[:])
                return

            for i in range(idx, len(candidates)):
                if res - candidates[i] < 0:
                    # break ### other options are larger than current one, if we have sorted the array
                    continue
                else:
                    path.append(candidates[i])
                    DFS(res-candidates[i], path, i)
                    path.pop() ### backtrack
        DFS(target, [], 0)
        return ans
