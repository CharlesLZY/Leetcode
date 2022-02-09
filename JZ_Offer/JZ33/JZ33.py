'''
JZ23 二叉搜索树的后序遍历序列

描述:
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回 true ,否则返回 false 。
假设输入的数组的任意两个数字都互不相同。
'''

# @param sequence List[int]
# @return bool

### Divide and Conquer Solution
### TC: O(n^2) and SC: O(n)
class Solution:
    def VerifySquenceOfBST(self, sequence):

        def check(low, high):
            if low >= high:
                return True

            root = sequence[high]
            right = high - 1
            left = low
            ### in BST, right branch must be larger than root and left branch
            while sequence[right] > root and right >= left: ### decide whether belongs to the right sub-tree
                right -= 1

            partition = right

            while right >= left: ### the remaining nodes are all belongs to left sub-tree
                if sequence[right] > root: ### check whether all nodes in left sub-tree are smaller than the root
                    return False
                right -= 1

            return check(low, partition) and check(partition+1, high-1)

        if len(sequence) == 0: ### corner case: empty tree
            return False

        return check(0, len(sequence)-1)


'''
The inorder traversal of binary search tree is a sorted array.
If we sort the postorder traversal sequence, then we will get the inorder sequence.
The inorder traversal and postorder traversal of the binary tree correspond to a stack push and pop sequence.
    2
   / \
  1   3
Inorder: push 1 push 2 push 3
Postorder: push 1 pop 1 push 2 push 3 pop 3 pop 2
Preorder: 2 1 3 (Also can be a postorder like below)
    3
   /
  1
   \
    2
'''


'''
可以把一种遍历顺序看成一个push顺序，然后把另外一种遍历顺序看成pop顺序，但树可以长成各种各样，将排序后的数组作为中序遍历可以确保这是一个BST
但这题中，只能把inorder(sorted array)当做push顺序，去检查post-order是不是合法的pop顺序
反过来，312这个case处理不了
'''

### Stack Solution: Check whether sequence is a valid stack pop sequence if we treat the inorder traverse sequence as the stack push order
### TC: O(nlogn) and SC: O(n)
class Solution:
    def VerifySquenceOfBST(self, sequence):

        if len(sequence) == 0: ### corner case: empty tree
            return False 

        inorder = sequence[:] ### stack push order
        inorder.sort()

        stack = []
        j = 0
        for i in range(len(inorder)):
            if inorder[i] == sequence[j]: ### immediate pop after push
                j += 1
                while len(stack) > 0 and sequence[j] == stack[-1]: ### trigger the pop chain 
                    stack.pop()
                    j += 1
            else:
                stack.append(inorder[i])
        while len(stack) > 0 and sequence[j] == stack[-1]: ### check the remaining node in the stack
            stack.pop()
            j += 1

        if len(stack) > 0:
            return False
        else:
            return True

'''
                1     |     1     |     2     |     2     |     3     |     3     
              2   3   |   3   2   |   1   3   |   3   1   |   1   2   |   2   1  
                      |           |           |           |           |               
pre-order:    1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
inorder:      2 1 3   |   3 1 2   |   1 2 3   |   3 2 1   |   1 3 2   |   2 3 1
post-order:   2 3 1   |   3 2 1   |   1 3 2   |   3 1 2   |   1 2 3   |   2 1 3


                1     |     1     |     2     |     2     |     3     |     3     
              2       |   3       |   1       |   3       |   1       |   2     
            3         | 2         | 3         | 1         | 2         | 1              
pre-order:    1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
inorder:      3 2 1   |   2 3 1   |   3 1 2   |   1 3 2   |   2 1 3   |   1 2 3
post-order:   3 2 1   |   2 3 1   |   3 1 2   |   1 3 2   |   2 1 3   |   1 2 3


                1     |     1     |     2     |     2     |     3     |     3     
              2       |   3       |   1       |   3       |   1       |   2     
                3     |     2     |     3     |     1     |     2     |     1              
pre-order:    1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
inorder:      2 3 1   |   3 2 1   |   1 3 2   |   3 1 2   |   1 2 3   |   2 1 3
post-order:   3 2 1   |   2 3 1   |   3 1 2   |   1 3 2   |   2 1 3   |   1 2 3


                1     |     1     |     2     |     2     |     3     |     3     
                  2   |       3   |       1   |       3   |       1   |       2  
                    3 |         2 |         3 |         1 |         2 |         1       
pre-order:    1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
inorder:      1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
post-order:   3 2 1   |   2 3 1   |   3 1 2   |   1 3 2   |   2 1 3   |   1 2 3


                1     |     1     |     2     |     2     |     3     |     3     
                  2   |       3   |       1   |       3   |       1   |       2  
                3     |     2     |     3     |     1     |     2     |     1       
pre-order:    1 2 3   |   1 3 2   |   2 1 3   |   2 3 1   |   3 1 2   |   3 2 1
inorder:      1 3 2   |   1 2 3   |   2 3 1   |   2 1 3   |   3 2 1   |   3 1 2
post-order:   3 2 1   |   2 3 1   |   3 1 2   |   1 3 2   |   2 1 3   |   1 2 3


push order: 3 1 2
3  3' 1  1' 2  2' ： pop order: 3 1 2
3  3' 1  2  2' 1' ： pop order: 3 2 1
3  1  1' 3' 2  2' ： pop order: 1 3 2
3  1  2  2' 1' 3' ： pop order: 2 1 3
3  1  1' 2  2' 3' ： pop order: 1 2 3
'''