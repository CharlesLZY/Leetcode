'''
Leetcode 315. Count of Smaller Numbers After Self

Description:
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
'''

# @param nums List[int]
# @return List[int]

'''
nums = [6,5,2,5,3,8,1]

        1
         \
          8
         /
        3
       / \
      2   5
         / \
        5   6


'''
### BST Solution 
### TC: O(nlogn) and SC: O(n)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0 ### number of left child

class Solution:
    def countSmaller(self, nums):
        ans = [0]*len(nums)
        def insertNode(root, val, i):
            if val <= root.val: ### trick: same number should be put into left branch
                root.count += 1
                if root.left:
                    insertNode(root.left, val, i)
                else: ### after each node is set, the ans[i] will never change
                    root.left = TreeNode(val) ### nums[:i] will not affect ans[i]
            elif val > root.val:
                ans[i] += root.count + 1 ### root's left child + root itself
                if root.right:
                    insertNode(root.right, val, i)
                else: ### after each node is set, the ans[i] will never change
                    root.right = TreeNode(val) ### nums[:i] will not affect ans[i]

        root = TreeNode(nums[-1]) ### trick: iterate the array in reverse
        for i in range(len(nums)-2, -1, -1):
            insertNode(root, nums[i], i) ### the left number will always be the child of right number

        return ans


### Merge Sort Solution
### TC: O(nlogn) and SC: O(n)
class Solution:
    def countSmaller(self, nums):
        ans = len(nums) * [0]
        arr = [(v, i) for i, v in enumerate(nums)]
        def mergeSort(arr):
            if len(arr) == 1:
                return 
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            mergeSort(left)
            mergeSort(right)
            merge(left, right, arr)

        def merge(left, right, arr):
            p1 = 0
            p2 = 0
            for i in range(len(left)+len(right)):
                if p1 < len(left) and p2 < len(right):
                    if left[p1][0] <= right[p2][0]: ### only left half will cause ans to update (only the former number can have smaller number in the behind)
                        arr[i] = left[p1]
                        ans[left[p1][1]] += i - p1 ### i - p1 means the number of how many values in right half have been set in the left half
                        p1 += 1
                    else:
                        arr[i] = right[p2]
                        p2 += 1
                elif p1 < len(left): ### the rest number in left half all have smaller number in right half
                    arr[i] = left[p1]
                    ans[left[p1][1]] += i - p1 ### i - p1 means the number of how many values in right half have been set in the left half
                    p1 += 1
                else:
                    arr[i] = right[p2]
                    p2 += 1
        mergeSort(arr)
        return ans


class Solution:
    def countSmaller(self, nums):
        ans = len(nums) * [0]
        arr = [(v, i) for i, v in enumerate(nums)]
        temp = [(v, i) for i, v in enumerate(nums)] ### auxiliary array
        def mergeSort(low, high):
            if low < high:
                mid = (low + high) // 2

                mergeSort(low, mid)
                mergeSort(mid+1, high)

                p = low
                q = mid+1
                while p <= mid and q <= high:
                    if arr[p][0] > arr[q][0]:
                        for i in range(p, mid+1):
                            ans[arr[i][1]] += 1
                        q += 1
                    else:
                        p += 1

                for i in range(low, high+1):
                    temp[i] = arr[i] ### temporarily store the array for convenience to merge

                p1 = low
                p2 = mid + 1
                for i in range(low, high+1):
                    if p1 <= mid and p2 <= high:
                        if temp[p1] <= temp[p2]:
                            arr[i] = temp[p1]
                            p1 += 1
                        else:
                            arr[i] = temp[p2]
                            p2 += 1
                    elif p1 <= mid:
                        arr[i] = temp[p1]
                        p1 += 1
                    else:
                        arr[i] = temp[p2]
                        p2 += 1
        mergeSort(0, len(arr)-1)
        return ans
