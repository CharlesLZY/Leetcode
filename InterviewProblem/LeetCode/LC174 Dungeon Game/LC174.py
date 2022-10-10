'''
Leetcode 174. Dungeon Game

Description:
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of m x n rooms laid out in a 2D grid. 
Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; 
other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example:
Input: dungeon = [[-2, -3, 3],
                  [-5,-10, 1],
                  [10, 30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 
if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
'''

# @param dungeon List[List[int]]
# @return int

'''
这题的trick在于要从终点开始
'''
### DP Solution
### TC: O(mn) and SC: O(mn)
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        DP_table = [[1]*n for _ in range(m)] ### DP[i][j] : minLife start from (i,j)
        minLife = 1 if dungeon[m-1][n-1] >= 0 else -dungeon[m-1][n-1]+1
        DP_table[m-1][n-1] = minLife

        for i in range(m-2, -1, -1):
            curCell = dungeon[i][n-1]
            nextMinLife = DP_table[i+1][n-1]
            DP_table[i][n-1] = max(1, nextMinLife - curCell)

        for j in range(n-2, -1, -1):
            curCell = dungeon[m-1][j]
            nextMinLife = DP_table[m-1][j+1]
            DP_table[m-1][j] = max(1, nextMinLife - curCell)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                curCell = dungeon[i][j]
                downDir = max(1, DP_table[i][j+1] - curCell)
                rightDir = max(1, DP_table[i+1][j] - curCell)
                DP_table[i][j] = min(downDir, rightDir)

        return DP_table[0][0]

### Wrong Answer 
### case: [[1,-3,3],[0,-2,0],[-3,-3,-3]]
### It will select down -> right -> right -> down instead of right -> right -> down -> down
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        DP_table = [[[-1,-1]]*n for _ in range(m)] ### DP[i][j] : (minLife, curLife) ### min life to get here and current life in this block
        minLife = 1 if dungeon[0][0] >= 0 else -dungeon[0][0]+1
        curLife = 1 + dungeon[0][0] if dungeon[0][0] >= 0 else 1
        DP_table[0][0] = [minLife, curLife]

        def calculate(curCell, prevMinLife, prevCurLife):
            minLife, curLife = -1, -1
            if prevCurLife + curCell > 0:
                minLife = prevMinLife
                curLife = prevCurLife + curCell
            else: 
                minLife = -(curCell + prevCurLife) + 1 + prevMinLife
                curLife = 1
            return [minLife, curLife]

        for i in range(1, m):
            curCell = dungeon[i][0]
            prevMinLife, prevCurLife  = DP_table[i-1][0][0], DP_table[i-1][0][1]
            DP_table[i][0] = calculate(curCell, prevMinLife, prevCurLife)


        for j in range(1,n):
            curCell = dungeon[0][j]
            prevMinLife, prevCurLife  = DP_table[0][j-1][0], DP_table[0][j-1][1]
            DP_table[0][j] = calculate(curCell, prevMinLife, prevCurLife)

        for i in range(1, m):
            for j in range(1, n):
                curCell = dungeon[i][j]
                upDir = calculate(curCell, DP_table[i][j-1][0], DP_table[i][j-1][1])
                leftDir = calculate(curCell, DP_table[i-1][j][0], DP_table[i-1][j][1])
                DP_table[i][j] = upDir if upDir[0] < leftDir[0] else leftDir

        return DP_table[m-1][n-1][0]

















        