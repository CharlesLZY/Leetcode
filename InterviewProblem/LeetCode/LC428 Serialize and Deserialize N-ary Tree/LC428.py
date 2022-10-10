'''
Leetcode 428. Serialize and Deserialize N-ary Tree

Description:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

LeetCode's level order traversal serialization format, where each group of children is separated by the null value.
Example:
                        1
        2      3                 4        5  
             6   7               8      9   10
                 11             12     13   
                 14
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''

# class Node(object):
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

'''
      0
  1   2   3
 4 5
BFS: 0,#,1,2,3,#,4,5,#,#,# (Leetcode上把tail #s都去掉了)

        1
  2  3     4     5
    6 7    8   9  10
      11   12  13
      14
0;#;2;3;4;5;#;#;6;7;#;8;#;9;10;#;#;11;#;12;#;13;#;#;14;#;#;#
每一层结束会有一个#分隔
除此之外, 假设第n-1层有i个node, 那么第n层会有i-1个#用来分隔第n-1层的i个node的children
第n层一定有i个#
'''
### BFS Solution (Leetcode Style)
### TC: O(n) and SC: O(n)
class Codec:
    def serialize(self, root):
        res = []
        if root: ### corner case
            cur_level = [root]

            while cur_level:
                res += [str(node.val) if node else '#' for node in cur_level] + ['#'] ### layer seperator
                next_level = []
                for node in cur_level:
                    if node:
                        next_level += [child for child in node.children] + [None] ### trick: use None as seperator and it will be converted to a group-children seperator '#'
                if next_level[-1] is None: # pop the last unnecessary separator: x None x None -> x None x
                    next_level.pop()

                ### trick: next_level will have at least as many group-children seperator as #nodes in the previous layer - 1
                # cur_level = next_level if len(next_level) != len(list(filter(None, cur_level)))-1 else []

                ### trick: if next_level has no node
                cur_level = next_level if len(list(filter(None, next_level))) > 0 else []

            return ';'.join(res)

        else:
            return res

    from collections import deque
    def deserialize(self, data):
        if data:
            src = deque(data.split(';'))
            root = Node(src.popleft(), [])
            cur_level = [root]
            src.popleft() ### level 0 seperator

            while src:
                next_level = []
                for node in cur_level:
                    while src:
                        child = src.popleft()
                        if  child != '#':
                            node.children.append(Node(child, []))
                        else: ### each node will have exactly one '#' either group-children seperator or layer seperator
                            break

                    next_level.extend(node.children)
                cur_level = next_level
            return root
        else: ### corner case
            return None


'''
      0
  1   2   3
     4 5  6
       7
DFS: 0 [ 1 2 [ 4 5 [ 7 ] ] 3 [ 6 ] ] 
'''
### My Ugly Solution
### TC: O(n) and SC: O(n)
class Codec:
    def serialize(self, root):
        res = []
        def DFS(node):
            nonlocal res
            res.append(str(node.val))
            if node.children:
                res.append('[')
                for child in node.children:
                    DFS(child)
                res.append(']')
        
        if root: ### corner case
            DFS(root)
        
        return ';'.join(res)
        
    def deserialize(self, data):
        def DFS(src):
            root = Node(src[0], [])
            i = 2
            while i < len(src)-1:
                j = i + 1
                if j < len(src)-1 and src[j] == '[':
                    n_lp = 1
                    j += 1 ### skip '['
                    while n_lp != 0:
                        if src[j] == '[':
                            n_lp += 1
                        elif src[j] == ']':
                            n_lp -= 1
                        j += 1
                root.children.append(DFS(src[i:j]))
                i = j
        
            return root

        if not data: ### corner case
            return None

        src = data.split(';')
        return DFS(src)