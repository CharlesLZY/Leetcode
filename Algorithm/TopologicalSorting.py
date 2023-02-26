'''
Topological sort is an algorithm that takes a directed acyclic graph(DAG) and 
returns the sequence of nodes where every node will appear before other nodes that it points to. 

Input:  
            
 ----> B --> C --- 
|            |    |      
|            |    |      F
A ---> D <---     |       
       |          |
        ----> E <-
             
Output: [A,F,B,C,D,E]

How does it work?
Keep popping the nodes with 0 in-degress from the graph.
       1     1
 ----> B --> C --- 
|            |    |      0
|      2     |    |      F
A ---> D <---     |       
0      |      2   |
        ----> E <-

=>
       0     1
       B --> C --- 
             |    |      
       1     |    |      
       D <---     |       
       |      2   |
        ----> E <-

=> 
             0
             C --- 
             |    |      
       1     |    |      
       D <---     |       
       |      2   |
        ----> E <-

=>            
       0              
       D            
       |      1   
        ----> E 

=>            
              0
              E 

'''

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    
    def addEdge(self, m, n): 
        self.graph[m].add(n)
        self.graph[n]
    
    def isAcyclic(self):
        nodes = list(self.graph.keys())
        visited = defaultdict(bool)
        lookup = defaultdict(bool) ### trick: temporarily look-up record to decide whether there is cycle in this round

        def findCycle(node): ### find cycle
            visited[node] = True
            lookup[node] = True
            for neighbour in self.graph[node]:
                if lookup[neighbour]: ### cyclic
                    return True
                elif not visited[neighbour]: ### trick: avoid repeated checks
                    if findCycle(neighbour):
                        return True
            lookup[node] = False ### reset, only being used for this round of cycle checking
            return False

        for node in nodes:
            if not visited[node] and findCycle(node): ### findCycle(node) equals to select the node first, check whether node itself has any prerequisite pointing to it
                return False
        return True

'''
If G is a DAG and (u,v) is an edge then for any DFS, f(u) > f(v) where f(.) is the finish time of DFS
Proof:
Case 1: s(u) < s(v) 
v is the descendant of u
Case 2: If s(v) < s(u)
If we discovered u in the course of DFS of v, then there must be a path from v to u, plus there is a edge (u,v), there must be a cycle
'''
### Store the order of being popped from the graph
def topologicalSort(graph):
    nodes = list(graph.keys())
    print(nodes)
    visited = defaultdict(bool)
    res = []

    def DFS(node, depth):
        visited[node] = True
        for succ in graph[node]:
            if not visited[succ]:
                DFS(succ, depth+1)
        res.append((node, depth))
    
    for node in nodes:
        if not visited[node]:
            DFS(node, 0)

    res.sort(key=lambda x:x[1]) ### this line must exists, DFS solution can not handle the case that descendant starts DFS before its ancestor
    
    return res

### Intuitive Version
# def topologicalSort(graph):
#     nodes = list(graph.keys())
#     in_degree = defaultdict(int)
#     for node in nodes:
#         for succ in graph[node]:
#             in_degree[succ] += 1
    
#     res = []
#     queue = [node for node in nodes if in_degree[node] == 0] ### zero in-degree nodes
#     while queue:
#         node = queue.pop(0)
#         res.append(node)

#         for succ in graph[node]:
#             in_degree[succ] -= 1
#             if in_degree[succ] == 0:
#                 queue.append(succ)
#     ### if res does not contain all nodes in the graph, then the graph has cycle
#     return res

'''
6 7
8 4
1 4 5
2 5
3 4 5
'''

g = Graph()
# g.addEdge(6,7)
# g.addEdge(8,4)
# g.addEdge(1,4)
# g.addEdge(4,1)
# g.addEdge(1,3)
# g.addEdge(4,5)
# g.addEdge(2,5)
# g.addEdge(3,4)


# g.addEdge(5, 3);

g.addEdge(0, 3);
g.addEdge(0, 2);
g.addEdge(3, 4);
g.addEdge(1, 4);
g.addEdge(2, 3);

g.addEdge(5, 3); ### unless we can ensure that ancestor always start DFS before its descendants

print(topologicalSort(g.graph))



