'''
Leetcode 51. N-Queens

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

[[".Q..",
  "...Q",
  "Q...",
  "..Q."],

  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."]]
'''

# @param n int
# @return List[List[str]]

### DFS Solution
### TC: O(n!) and SC: O(n^2)
class Solution:
    def solveNQueens(self, n):
        result = []
        ### state is a list the i element is the col of the queen in the i row
        def create_board(state): ### for the output form
            board = []
            for col in state:
                line = ["."] * (n-1)
                line.insert(col, "Q")
                board.append("".join(line)) ### connect each char in row with "", row is a list with char elements
            return board 

        def valid(state, cur_row, candidate_col):
            for row in range(cur_row): ### cur_row is the new candidate's row
                col = state[row]
                ### check diagonal and whether there is the same col (no need to check same row because we only asign one queen per row)
                if abs(row - cur_row) == abs(col- candidate_col) or col == candidate_col: ### smart way to check diagonal
                    return False
            return True

        ### state is a list where the ith element is the col of the queen in the i row
        ### [1, 3, 0, 2] = [".Q..",
        ###                 "...Q",
        ###                 "Q...",
        ###                 "..Q."]
        def DFS(state, row):
            if row == n:
                result.append(state[:])
                return
            for col in range(n):
                if valid(state, row, col):
                    state[row] = col
                    DFS(state, row+1) ### we move row by row (no need to check row for validity)

        empty_state = [None for _ in range(n)]
        DFS(empty_state, 0)

        for i in range(len(result)):
            result[i] = create_board(result[i])

        return result


