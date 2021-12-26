'''
JZ37 序列化二叉树

描述：
请实现两个函数，分别用来序列化和反序列化二叉树，不对序列化之后的字符串进行约束，
但要求能够根据序列化之后的字符串重新构造出一棵与原二叉树相同的树。

二叉树的序列化(Serialize)是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树等遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过某种符号表示空节点（#）

二叉树的反序列化(Deserialize)是指：根据某种遍历顺序得到的序列化字符串结果，重构二叉树。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### DFS Solution 
### TC: O(n) and SC: O(n)
class Solution:
    ## recursive version
    def Serialize(self, root):
        def encode(node, string):
            if node:
                string += str(node.val) + ';' ### string is immutable
                string = encode(node.left, string)
                string = encode(node.right, string)
            else:
                string += "#;"
            return string
        return encode(root, "")

    def Serialize(self, root):
        if root:
            return str(root.val) + ';' + self.Serialize(root.left) + self.Serialize(root.right)
        else:
            return "#;"

    def Deserialize(self, s):
        def decode(nodes):
            if nodes[0] == '#':
                nodes.pop(0)
                return None
            root = TreeNode(int(nodes.pop(0)))
            
            root.left = decode(nodes)
            root.right = decode(nodes)
            return root
        nodes = s.split(';')
        return decode(nodes)

    ### stack version
    def Serialize(self, root):
        stack = [root]
        string = ""
        while stack:
            node = stack.pop()
            if node is None:
                string += '#;'
            else:
                string += str(node.val) + ';'
                stack.append(node.right) ### Key point: Because of LIFO, we should push right branch first
                stack.append(node.left) ### Key point: Because of LIFO, we should push right branch first
        return string

    def Deserialize(self, s):
        nodes = s.split(';')
        if nodes[0] == '#': ### corner case
            return None
        root = TreeNode(int(nodes.pop(0)))
        stack = [(root, "right"), (root, "left")]
        while stack:
            parent, lr = stack.pop()
            val = nodes.pop(0)
            if val != '#':
                node = TreeNode(int(val))
                if lr == "left":
                    parent.left = node
                elif lr == "right":
                    parent.right = node
                stack.append((node, "right")) ### Key point: Because of LIFO, we should push right branch first
                stack.append((node, "left")) ### Key point: Because of LIFO, we should push right branch first

        return root

### BFS Solution (Queue)
### TC: O(n) and SC: O(n)
class Solution:
    def Serialize(self, root):
        queue = [root]
        string = ""
        while queue:
            node = queue.pop(0)
            if node is None:
                string += '#;'
            else:
                string += str(node.val) + ';'
                queue.append(node.left) ### FIFO
                queue.append(node.right) ### FIFO
        return string

    def Deserialize(self, s):
        nodes = s.split(';')
        if nodes[0] == '#': ### corner case
            return None

        root = TreeNode(int(nodes.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)

            if nodes[0] != '#':
                node.left = TreeNode(int(nodes[0]))
                queue.append(node.left)
            nodes.pop(0)

            if nodes[0] != '#':
                node.right = TreeNode(int(nodes[0]))
                queue.append(node.right)
            nodes.pop(0)

        return root


