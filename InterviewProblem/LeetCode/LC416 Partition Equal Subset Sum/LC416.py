'''
Leetcode 416. Partition Equal Subset Sum

Description:
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into 
two subsets such that the sum of elements in both subsets is equal.
'''

# @param nums List[int]
# @return bool

'''
If two subset sum are equal, they must be half of the sum of the whole array.
Refer to LC494
'''

### Brute Recursion Solution
### TC: O(2^n) and SC: O(n)
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        ### since array only contains positive integers
        if target % 2 == 1:
            return False
        else:
            target = target // 2 # If two subset sum are equal, they must be half of the sum of the whole array.
        @lru_cache(maxsize=None) ### Magic Line
        def DFS(idx, res):
            if res == target:
                return True
            if idx == len(nums):
                return False

            return DFS(idx+1, res) or DFS(idx+1, res+nums[idx])

        return DFS(0, 0)


### Recursion Solution with Memoization (Modified from LC494)
### TC: O(m*n) and SC: O(m*n) where m = sum(nums) // 2
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        ### since array only contains positive integers
        if target % 2 == 1:
            return False
        else:
            target = target // 2 # If two subset sum are equal, they must be half of the sum of the whole array.

        DP_table = {} ### { (curIdx, curSum) : whether the remaining numbers in the array can achieve the target }
        def DFS(idx, res):
            if idx == len(nums):
                return True if res == target else False
            if (idx, res) in DP_table:
                return DP_table[(idx, res)]

            DP_table[(idx, res)] = DFS(idx+1, res+nums[idx]) or DFS(idx+1, res)
            return DP_table[(idx, res)]

        return DFS(0, 0)

### Optimized Recursion Solution with Memoization
### TC: O(m*n) and SC: O(m*n) where m = sum(nums) // 2
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        ### since array only contains positive integers
        if target % 2 == 1:
            return False
        else:
            target = target // 2 # If two subset sum are equal, they must be half of the sum of the whole array.

        ### DP[curIdx][curSum] : whether nums[curIdx:] can achieve the target if we have the cumulative sum equals curSum
        DP_table = [[None] * (sum(nums) + 1) for _ in range(len(nums) + 1)]  
        def DFS(idx, res):
            if idx == len(nums):
                return True if res == target else False ### this line can acelerate 30%
            if DP_table[idx][res] is not None:
                return DP_table[idx][res]

            DP_table[idx][res] = DFS(idx+1, res+nums[idx]) or DFS(idx+1, res)
            return DP_table[idx][res]

        return DFS(0, 0)

### DP Solution
### TC: O(m*n) and SC: O(m*n) where m = sum(nums) // 2
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        ### since array only contains positive integers
        if target % 2 == 1:
            return False
        else:
            target = target // 2 # If two subset sum are equal, they must be half of the sum of the whole array.
        
        ### DP[i][j] : whether nums[:i] can sum up to j
        DP_table = [[False] * (target + 1) for _ in range(len(nums) + 1)] 
        DP_table[0][0] = True
        for i in range(1, len(nums) + 1):
            cur = nums[i - 1]
            for j in range(target + 1):
                if j < cur:
                    DP_table[i][j] = DP_table[i - 1][j]
                else:
                    DP_table[i][j] = DP_table[i - 1][j] or DP_table[i - 1][j - cur]
        return DP_table[len(nums)][target]