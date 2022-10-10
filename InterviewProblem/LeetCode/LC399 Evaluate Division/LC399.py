'''
Leetcode 399. Evaluate Division

Description:
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [A_i, B_i] and values[i] represent the equation A_i / B_i = values[i]. 
Each A_i or B_i is a string that represents a single variable.

You are also given some queries, where queries[j] = [C_j, D_j] represents the jth query 
where you must find the answer for C_j / D_j = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero 
and that there is no contradiction.

Example:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
'''

# @param equations List[List[str]] 
# @param values List[float]
# @param queries List[List[str]]
# @return List[float]


'''
The key idea of this problem is to treat the problem as a graph problem.
If we have a/b = 2 and b/c = 3. We can know b/a = 1/2 and c/b = 1/3.
we have the graph:
      1/2  1/3
      <-   <-  
    a    b    c        a/c : path a->c = 2*3 = 6 
      ->   ->
      2     3
'''
### Graph Search Solution
class Solution:
    def calcEquation(self, equations, values, queries):
        ### build graph
        graph = {} ### use nested dict to simulate graph because we need to store the edge weight
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            if dividend not in graph:
                graph[dividend] = {}
            graph[dividend][divisor] = values[i]
            if divisor not in graph:
                graph[divisor] = {}
            graph[divisor][dividend] = 1/values[i]

        def findPath(start, end, res, visited):
            if start in visited:
                return -1.0
            visited.append(start)
            for neighbour in graph[start]:
                temp = res * graph[start][neighbour]
                if neighbour == end:
                    return temp
                else:
                    result = findPath(neighbour, end, temp, visited)
                    if result != -1.0:
                        return result
            return -1.0

        ans = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph: ### corner case
                ans.append(-1.0)
            else:
                ans.append(findPath(q[0], q[1], 1, [])) ### each time we change the start node, we need to have a new visited list to start a new round graph search
        return ans


### Another version
class Solution:
    def calcEquation(self, equations, values, queries):
        ### build graph
        graph = {} ### use nested dict to simulate graph
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            if dividend not in graph:
                graph[dividend] = {}
            graph[dividend][divisor] = values[i]
            if divisor not in graph:
                graph[divisor] = {}
            graph[divisor][dividend] = 1/values[i]

        
        def findPath(start, end, res, visited):
            if start == end: ### corner case
                return 1
            visited.append(start)
            for neighbour in graph[start]:
                if neighbour not in visited:
                    temp = res * graph[start][neighbour]
                    if neighbour == end:
                        return temp
                    else:

                        result = findPath(neighbour, end, temp, visited)
                        if result != -1.0:
                            return result
            return -1.0

        ans = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph: ### corner case
                ans.append(-1.0)
            else:
                ans.append(findPath(q[0], q[1], 1, []))
        return ans