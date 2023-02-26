'''
### Disjoint Set (Union-Find)
Disjoint set is a data structure that stores a collection of disjoint (non-overlapping) sets.
In practice, the implementation of disjoint set is a forest. 
The disjoint set supports two operations: find the root of a node recursively and union two disjoint trees
Find operation: Each node has its parent and the disjoint set can find the root recursively.
Union operation: Set parent[x] = find(y)
'''

'''
The trick is how to make find operation more efficient.
We should always let the shorter tree to attach the higher one. 
In this way, the union's height is the same as the higher tree.
The efficiency of find operation remains.
'''
### Standard Version (Optimized through rank)
class DisjointSet:
    def __init__(self, size):
        ### the root can be considered as current immediate-parent
        self.root = [i for i in range(size)] ### at the beginning, each node point to itself
        self.rank = [1] * size ### 空间复杂度可以进一步优化, 现在如果root[i] = i表明是一个根节点, 那我们也可以用root[i] = -rank来标识, 这样就不需要再维护rank数组了

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) ### trick: update the root[x] since we have find its root
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

### More Elegant Version
class DisjointSet:
    def __init__(self, size):
        self.root = [-1 for _ in range(size)] ### root[x] < 0 means that it is the root of a disjoint tree

    def find(self, x):
        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.root[root_x] < self.root[root_y]:
                self.root[root_y] = root_x
            elif self.root[root_x] > self.root[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.root[root_x] -= 1

'''
we cannot use union-find to detect cycles in a directed graph. 
This is because a directed graph cannot be represented using the disjoint set.
When we say 'a union b' we cannot make out the direction of edge.
But, incase of undirected graphs, each connected component is equivalent to a set. So union-find can be used to detect a cycle. 
Whenever you try to perform union on two vertices belonging to the same connected component, we can say that cycle exists.
'''