'''
Leetcode 297. Serialize and Deserialize Binary Tree

Description:
Serialization is the process of converting a data structure or object into a sequence of bits so that 
it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on 
how your serialization/deserialization algorithm should work. You just need to ensure that a 
binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
     0
  1     2
      3   4
           5

DFS: 0;1;#;#;2;3;#;#;4;#;5;#;#;
'''
### DFS Solution
### TC: O(n) and SC: O(n)
class Codec:
    ## recursive version
    def serialize(self, root):
        def encode(node, string):
            if node:
                string += str(node.val) + ';' ### trick: ';' is for convenience to split (数字必须有分隔，否则分不清是几个数)
                string = encode(node.left, string)
                string = encode(node.right, string)
            else:
                string += "#;"
            return string
        return encode(root, "")

    def serialize(self, root):
        if root is None:
            return "#;"
        else:
            return str(root.val) + ';' + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        def decode(nodes):
            if nodes[0] == '#':
                nodes.pop(0)
                return None
            else:
                root = TreeNode(nodes.pop(0)) ### simulate DFS
                root.left = decode(nodes)
                root.right = decode(nodes)
                return root
        
        nodes = data.split(';')

        return decode(nodes)

    ### stack version
    def serialize(self, root):
        stack = [root]
        string = ""
        while stack:
            node = stack.pop()
            if node is None:
                string += "#;"
            else:
                string += str(node.val) + ';' ### trick: ';' is for convenience to split (数字必须有分隔，否则分不清是几个数)
                stack.append(node.right) ### Key point: Because of LIFO, we should push right branch first
                stack.append(node.left) 
        return string

    def deserialize(self, data):
        nodes = data.split(';')
        if nodes[0] == '#': ### corner case
            return None

        root = TreeNode(nodes.pop(0))
        stack = [(root, "right"), (root, "left")]
        while stack:
            parent, lr = stack.pop()
            val = nodes.pop(0)
            if val != '#':
                node = TreeNode(val)
                if lr == "left":
                    parent.left = node
                elif lr == "right":
                    parent.right = node
                stack.append((node, "right")) ### Key point: Because of LIFO, we should push right branch first
                stack.append((node, "left")) ### Key point: Because of LIFO, we should push right branch first

        return root


'''
     0
  1     2
      3   4
           5

BFS: 0;1;2;#;#;3;4;#;#;#;5;#;#;
'''
### BFS Solution (Queue)
### TC: O(n) and SC: O(n)
class Codec:
    def serialize(self, root):
        queue = [root]
        string = ""
        while queue:
            node = queue.pop(0)
            if node is None:
                string += "#;"
            else:
                string += str(node.val) + ';'
                queue.append(node.left) ### FIFO
                queue.append(node.right) ### FIFO
        return string

    def deserialize(self, data):
        nodes = data.split(';')
        if nodes[0] == '#': ### corner case
            return None

        root = TreeNode(nodes.pop(0)) 
        queue = [root]
        while queue:
            node = queue.pop(0)

            if nodes[0] != '#':
                node.left = TreeNode(nodes[0])
                queue.append(node.left)
            nodes.pop(0)

            if nodes[0] != '#':
                node.right = TreeNode(nodes[0])
                queue.append(node.right)
            nodes.pop(0)

        return root