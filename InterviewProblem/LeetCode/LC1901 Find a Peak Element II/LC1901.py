'''
Leetcode LC1901 Find a Peak Element II

Description:
A peak element in a 2D grid is an element that is strictly greater than all of 
its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, 
find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
Constraint: No two adjacent cells are equal. All mat[i][j] > 0.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
'''

# @param mat List[List[ints]]
# @return List[int]

'''
The key of binary search is that we must ensure that there is a solution in the half we selected.

mat[i][j] is the max in the ith row.
mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i][j+1]
if mat[i-1][j] > mat[i][j] we can know mat[i-1][j] > the whole ith row
then we get mat[i-1][j] is larger than four edges, we can conclude that there must be somehow a peak on the up half (imagine the function surface) 
          mat[i-1][j]
        ...         ...
        /             \
      ...             ...     
 left boundary     right boundary

elif mat[i+1][j] > mat[i][j]
else mat[i][j] is the peak

-1 -1 -1 -1 -1 -1 -1 -1 
-1                   -1
-1                   -1
-1       max         -1
-1                   -1
-1                   -1
-1 -1 -1 -1 -1 -1 -1 -1 
'''

### TC: O(mlogn) and SC: O(1)
class Solution:
    def findPeakGrid(self, mat):
        def findMAX(row):
            idx = 0
            MAX = -1
            for i in range(len(row)):
                if row[i] > MAX:
                    idx = i
                    MAX = row[i]
            return idx

        m, n = len(mat), len(mat[0])
        lp = 0 ### up pointer
        rp = m-1 ### down pointer
        while lp < rp:
            mid = (lp + rp) // 2
            idx = findMAX(mat[mid])
            if mid-1 >= 0 and mat[mid][idx] < mat[mid-1][idx]:
                rp = mid-1
            elif mid+1 < m and mat[mid][idx] < mat[mid+1][idx]:
                lp = mid+1
            else:
                return [mid, idx]
        return [lp, findMAX(mat[lp])]














