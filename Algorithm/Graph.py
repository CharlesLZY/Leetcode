from collections import defaultdict
def addEdge(graph, v1, v2, directed=True):
    graph[v1].add(v2)
    if not directed:
        graph[v2].add(v1)
    else:
        graph[v2] ### initialize the vertex


### 图是否有环
### DFS Solution
### 有向图
def isDGAcyclic(graph):
    nodes = list(graph.keys())
    visited = defaultdict(bool)
    lookup = defaultdict(bool) ### trick: temporarily look-up record to decide whether there is cycle in this round

    def findCycle(node): ### find cycle
        visited[node] = True
        lookup[node] = True
        for neighbour in graph[node]:
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

### 无向图
### Trick: check prev to avoid one-edge-cycle
def isUDGAcyclic(graph):
    nodes = list(graph.keys())
    visited = defaultdict(bool)
    lookup = defaultdict(bool) ### trick: temporarily look-up record to decide whether there is cycle in this round

    def findCycle(node, prev): ### find cycle
        visited[node] = True
        lookup[node] = True
        for neighbour in graph[node]:
            if neighbour != prev and lookup[neighbour]: ### cyclic
                return True
            elif not visited[neighbour]: ### trick: avoid repeated checks
                if findCycle(neighbour, node):
                    return True
        lookup[node] = False ### reset, only being used for this round of cycle checking
        return False
    
    prev = None
    for node in nodes:
        if not visited[node] and findCycle(node, prev): ### findCycle(node) equals to select the node first, check whether node itself has any prerequisite pointing to it
            return False
        prev = node
    return True


### Topological Sort Solution
### 有向图
def isDGAcyclic(graph):
    nodes = list(graph.keys())
    in_degree = defaultdict(int)
    for node in nodes:
        for succ in graph[node]:
            in_degree[succ] += 1
    
    res = []
    queue = [node for node in nodes if in_degree[node] == 0] ### zero in-degree nodes
    while queue:
        node = queue.pop(0)
        res.append(node)

        for succ in graph[node]:
            in_degree[succ] -= 1
            if in_degree[succ] == 0:
                queue.append(succ)
    
    return len(res) == len(nodes)

### 无向图
### Trick: Push nodes with in-degree = 1 into queue
def isUDGAcyclic(graph):
    nodes = list(graph.keys())
    in_degree = defaultdict(int)
    for node in nodes:
        for succ in graph[node]:
            in_degree[succ] += 1
    
    res = []
    queue = [node for node in nodes if in_degree[node] <= 1] ### one in-degree nodes
    while queue:
        node = queue.pop(0)
        res.append(node)

        for succ in graph[node]:
            in_degree[succ] -= 1
            if in_degree[succ] == 1: ### Trick: at least 1 in-degree from its previous node
                queue.append(succ)
    
    return len(res) == len(nodes)

graph1 = defaultdict(set)
addEdge(graph1, 0, 1, True)
addEdge(graph1, 1, 2, True)
addEdge(graph1, 2, 4, True)
addEdge(graph1, 2, 5, True)
addEdge(graph1, 4, 7, True)
addEdge(graph1, 5, 6, True)
addEdge(graph1, 6, 7, True)

### acyclic
addEdge(graph1, 1, 3, True)
addEdge(graph1, 3, 4, True)

### cyclic
# addEdge(graph1, 4, 3, True)
# addEdge(graph1, 3, 1, True)


graph2 = defaultdict(set)
addEdge(graph2, 0, 1, False)
addEdge(graph2, 1, 2, False)
addEdge(graph2, 1, 3, False)
addEdge(graph2, 2, 4, False)
addEdge(graph2, 2, 5, False)
addEdge(graph2, 5, 6, False)
addEdge(graph2, 6, 7, False)

### cyclic
addEdge(graph2, 3, 4, False)
addEdge(graph2, 4, 7, False)

# print(isDGAcyclic(graph1))
print(isUDGAcyclic(graph2))