'''
JZ59 滑动窗口的最大值

描述：
给定一个长度为 n 的数组 num 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。

例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

窗口大于数组长度或窗口长度为0的时候，返回空。
'''

# @param nums List[int] 
# @param size int 
# @return List[int]

### TC: O(n) and SC: O(k)
class Solution:
    def maxInWindows(self, nums, size):
        if len(nums) == 0 or size == 0: ### corner case
            return []
        ans = []

        aux = [] ### maintain a sorted sliding window, storing the index of the number

        for i in range(len(nums)):
            ### maintain aux array sorted
            while aux and nums[aux[-1]] < nums[i]:
                aux.pop() ### this numbers are not important, we only care the max in current window
            aux.append(i) ### store the index

            ### check whether the max is expired
            if aux[0] + size == i:
                aux.pop(0)

            if i+1 >= size:
                ans.append(nums[aux[0]])

        return ans



