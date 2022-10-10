'''
JZ12 矩阵中的路径

描述：
请设计一个函数，用来判断在一个n乘m的矩阵中是否存在一条包含某长度为len的字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
'''

# @param matrix List[List[str]] 
# @param word str
# @return bool

### TC: O(m*n*k^3) (3 possible directions to go) and SC: O(k)
class Solution:
    def hasPath(self, matrix, word):
        h, w = len(matrix), len(matrix[0])
        
        visited = []
        def DFS(start, k):
            if k == len(word):
                return True
            y, x = start
            visited.append(start)
            if (y-1, x) not in visited and y-1 >= 0 and matrix[y-1][x] == word[k]:
                if DFS((y-1, x), k+1):
                    return True
            if (y, x-1) not in visited and x-1 >= 0 and matrix[y][x-1] == word[k]:
                if DFS((y, x-1), k+1):
                    return True
            if (y+1, x) not in visited and y+1 < h and matrix[y+1][x] == word[k]:
                if DFS((y+1, x), k+1):
                    return True
            if (y, x+1) not in visited and x+1 < w and matrix[y][x+1] == word[k]:
                if DFS((y, x+1), k+1):
                    return True
            visited.pop() ### recursive version can do backtrack, stack version can not
            return False

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == word[0]:
                    if DFS((i,j), 1):
                        return True
        return False

### Awkward Stack Solution
class Solution:
    def hasPath(self, matrix, word):
        h, w = len(matrix), len(matrix[0])
        
        def DFS(start):
            stack = [(start, [])]
            while stack:
                cur, visited = stack.pop()
                k = len(visited) + 1
                if k == len(word):
                    return True
                
                visited.append(cur)
                y, x = cur
                
                if (y-1, x) not in visited and y-1 >= 0 and matrix[y-1][x] == word[k]:

                    stack.append(((y-1,x), visited[:]))
                if (y, x-1) not in visited and x-1 >= 0 and matrix[y][x-1] == word[k]:

                    stack.append(((y,x-1), visited[:]))
                if (y+1, x) not in visited and y+1 < h and matrix[y+1][x] == word[k]:

                    stack.append(((y+1,x), visited[:]))
                if (y, x+1) not in visited and x+1 < w and matrix[y][x+1] == word[k]:

                    stack.append(((y,x+1), visited[:]))

            return False


        for i in range(h):
            for j in range(w):
                if matrix[i][j] == word[0]:
                    if DFS((i,j)):
                        return True
        return False







