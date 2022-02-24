'''
Leetcode 1262. Greatest Sum Divisible by Three

Description:
Given an array nums of integers, we need to find the maximum possible sum of 
elements of the array such that it is divisible by three.

Constraints:
- 1 <= nums[i] <= 10^4
'''

# @param nums List[int]
# @return int


'''
因为这题都是正数, 我们把所有数分成被3整除余0、1、2
首先所有能被3整除的数我们肯定都要
假设我们有m个数被3整除余2, 因为3个被3整除的数加起来一定能被3整除(如果取m-3个, 那么为什么不取m个呢)
所以我们其实就是考虑取x = m、m-1、m-2个被3整除余2的数
同理假设我们有n个数被3整除余1, 我们也只考虑取y = n、n-1、n-2个
然后排列组合, 看看那种情况下能被3整除, 且和最大
(1*x + 2*y) % 3 = 0

还有一种方法
看看totalSum % 3等于几
然后分情况讨论删掉多少个被3整除余1或者2的数
'''
### Intuitive Mathematic Solution
### TC: O(n) and SC: O(n)
class Solution:
    def maxSumDivThree(self, nums):
        def find2Min(arr):
            maxHeap = []
            if arr[0] > arr[1]:
                maxHeap = [arr[0], arr[1]]
            else:
                maxHeap = [arr[1], arr[0]]
            for i in range(2, len(arr)):
                if arr[i] < maxHeap[0]:
                    if arr[i] >= maxHeap[1]:
                        maxHeap[0] = arr[i]
                    else:
                        maxHeap[0] = maxHeap[1]
                        maxHeap[1] = arr[i]
            return maxHeap

        totalSum = sum(nums)
        if totalSum % 3 == 0:
            return totalSum
        arr1 = []
        arr2 = []
        for n in nums:
            if n % 3 == 1:
                arr1.append(n)
            elif n % 3 == 2:
                arr2.append(n)
        if totalSum % 3 == 1:
            ### del 1 * %3==1
            ### del 2 * %3==2
            ### del 1 * %3==2 and 2 * %3==1 (must be worse than the first choice)
            if len(arr1) >= 1 and len(arr2) >= 2:
                if min(arr1) > sum(find2Min(arr2)):
                    return totalSum - sum(find2Min(arr2))
                else:
                    return totalSum - min(arr1)

            elif len(arr1) >= 1:
                return totalSum - min(arr1)

            else: ### len(arr2) >= 2
                return totalSum - sum(find2Min(arr2))


        elif totalSum % 3 == 2:
            ### del 2 * %3==1
            ### del 1 * %3==2
            if len(arr1) >= 2 and len(arr2) >= 1:
                if sum(find2Min(arr1)) > min(arr2):
                    return totalSum - min(arr2)
                else:
                    return totalSum - sum(find2Min(arr1))

            elif len(arr1) >= 2:
                return totalSum - sum(find2Min(arr1))
                
            else: ### len(arr2) >= 1
                return totalSum - min(arr2)

'''
DP[i][j] means the maximum possible sum (%3==j) end at i
1. pick nums[i]
if nums[i]%3 == 0:
    DP[i][0] = DP[i-1][0] + nums[i]
    DP[i][1] = DP[i-1][1] + nums[i]
    DP[i][2] = DP[i-1][2] + nums[i]
if nums[i]%3 == 1:
    DP[i][0] = DP[i-1][2] + nums[i]
    DP[i][1] = DP[i-1][0] + nums[i]
    DP[i][2] = DP[i-1][1] + nums[i]
if nums[i]%3 == 2:
    DP[i][0] = DP[i-1][1] + nums[i]
    DP[i][1] = DP[i-1][2] + nums[i]
    DP[i][2] = DP[i-1][0] + nums[i]
2. not pick nums[i]
DP[i][j] = DP[i-1][j]

DP[i] = max(pick nums[i], not pick nums[i])
'''
### DP Solution 
### TC: O(n) and SC: O(n) (can be optimized to SC = O(1) )
class Solution:
    def maxSumDivThree(self, nums):
        DP_table = [[0]*3 for _ in range(len(nums)+1)]
        DP_table[0][0] = 0
        DP_table[0][1] = float("-inf")
        DP_table[0][2] = float("-inf")

        for i in range(1, len(nums)+1):
            k = nums[i-1] % 3
            for j in range(3):
                DP_table[i][j] = max(DP_table[i-1][j], DP_table[i-1][(j-k+3)%3] + nums[i-1])

        return DP_table[-1][0]

### DP Solution 
### TC: O(n) and SC: O(1)
class Solution:
    def maxSumDivThree(self, nums):
        DP = [0, float("-inf"), float("-inf")] 
        for i in range(1, len(nums)+1):
            k = nums[i-1] % 3
            temp = DP[:]
            for j in range(3):
                DP[j] = max(temp[j], temp[(j-k+3)%3] + nums[i-1])

        return DP[0]
