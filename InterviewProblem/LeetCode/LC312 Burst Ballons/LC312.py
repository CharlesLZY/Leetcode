'''
Leetcode 312. Burst Balloons

Description:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
'''

# @param nums List[int] 
# @return int

### Backtrack Solution
class Solution:
    MAX = float("-inf")
    def maxCoins(self, nums):
        self.MAX = float("-inf")
        def DFS(res):
            if len(nums) == 0:
                self.MAX = max(self.MAX, res)
                return
            for i in range(len(nums)):
                cur = nums[i]
                bonus = cur * (nums[i-1] if i-1>=0 else 1) * (nums[i+1] if i+1 < len(nums) else 1)
                nums.pop(i)
                DFS(res+bonus)
                nums.insert(i, cur) ### back track
        DFS(0)
        return self.MAX


'''
动态规划要干两件事：
1. 找到彼此独立的最优子结构 (Optimal Substructure)
2. 找到子结构之间的递推关系 (Overlapping Sub-problems)
对于这道题，如果用打爆一个气球作为递推关系，会发现：打爆一个气球之后，左右两边的子问题不是独立的。
所以我们要反过来，我们指定一个气球最后打爆，这样其左右两边的子问题就是独立的了。 
DP[i][j] = max(DP[i][k-1]+DP[k+1][j]+nums[i-1]*nums[k]*nums[j+1])
'''
### DP Solution
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1] ### for convenience, padding the array with 1
        DP_table = [[float("-inf")]*len(nums) for _ in range(len(nums))]
        def DP(i,j): ### DP with memorization
            if j < i: ### if we choose the left/right-most balloon to be the last one to burst, the leftMAX/ rightMAX should be 0
                return 0 
            if DP_table[i][j] != float("-inf"):
                return DP_table[i][j]

            for k in range(i, j+1): ### balloon to burst in [i, j]
                leftMAX = DP(i, k-1)
                rightMAX = DP(k+1,j)
                cur = nums[i-1] * nums[j+1] * nums[k]
                DP_table[i][j] = max(DP_table[i][j], cur + leftMAX + rightMAX)

            return DP_table[i][j]

        return DP(1, len(nums)-2)

### Optimized DP Solution
class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1] ### for convenience, padding the array with 1
        DP_table = [[float("-inf")]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)): ### initialize DP table
            for j in range(len(nums)):
                if i > j: ### DP[i][j] should be 0 if i > j 
                    DP_table[i][j] = 0 

        for size in range(1, n+1): ### size of sub problem, size = j-i for DP[i][j]
            for lp in range(1, n-size+1+1): ### left boundary of the sub problem
                rp = lp + size - 1 ### right boundary of the sub problem
                for k in range(lp, rp+1):
                    DP_table[lp][rp] = max(DP_table[lp][rp], DP_table[lp][k-1] + DP_table[k+1][rp] + nums[k]*nums[lp-1]*nums[rp+1])

        return DP_table[1][n]



