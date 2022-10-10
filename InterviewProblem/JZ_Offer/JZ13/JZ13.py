'''
JZ13 机器人的运动范围

描述：
地上有一个 rows 行和 cols 列的方格。坐标从 [0,0] 到 [rows-1,cols-1] 。一个机器人从坐标 [0,0] 的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 threshold 的格子。 例如，
当 threshold 为 18 时，机器人能够进入方格   [35,37] ，因为 3+5+3+7 = 18。但是，它不能进入方格 [35,38] ，
因为 3+5+3+8 = 19 。请问该机器人能够达到多少个格子？
'''

# @param threshold int
# @param rows int 
# @param cols int
# @return int

### TC: O(mn) and SC: O(mn)
class Solution:
    def movingCount(self, threshold, rows, cols):
        def check(x, y):

            res = 0
            while x // 10 > 0:
                res += x % 10
                x = x // 10
            res += x % 10
            while y // 10 > 0:
                res += y % 10
                y = y // 10
            res += y % 10

            return res <= threshold

        ans = 0
        visited = [(0,0)]
        stack = [(0,0)]

        while stack:
            y, x = stack.pop()
            
            ans += 1

            if (y-1, x) not in visited and y-1 >= 0 and check(y-1, x):
                stack.append((y-1,x))
                visited.append((y-1,x))
            if (y+1, x) not in visited and y+1 < rows and check(y+1, x):
                stack.append((y+1,x))
                visited.append((y+1,x))
            if (y, x-1) not in visited and x-1 >= 0 and check(y, x-1):
                stack.append((y,x-1))
                visited.append((y,x-1))
            if (y, x+1) not in visited and x+1 < cols and check(y, x+1):
                stack.append((y,x+1))
                visited.append((y,x+1))

        return ans ### return len(visited)


### Recursive Solution
class Solution:
    def movingCount(self, threshold, rows, cols):
        self.visited = []
        self.ans = 0

        def check(x, y):

            res = 0
            while x // 10 > 0:
                res += x % 10
                x = x // 10
            res += x % 10
            while y // 10 > 0:
                res += y % 10
                y = y // 10
            res += y % 10

            return res <= threshold

        
        def DFS(start):
            y, x = start
            self.ans += 1
            if (y-1, x) not in self.visited and y-1 >= 0 and check(y-1, x):
                
                self.visited.append((y-1,x))
                DFS((y-1,x))
            if (y+1, x) not in self.visited and y+1 < rows and check(y+1, x):
                
                self.visited.append((y+1,x))
                DFS((y+1,x))
            if (y, x-1) not in self.visited and x-1 >= 0 and check(y, x-1):
                
                self.visited.append((y,x-1))
                DFS((y,x-1))
            if (y, x+1) not in self.visited and x+1 < cols and check(y, x+1):
                
                self.visited.append((y,x+1))
                DFS((y,x+1))

        self.visited.append((0,0))
        DFS((0,0))
        return self.ans ### return len(self.visited)
