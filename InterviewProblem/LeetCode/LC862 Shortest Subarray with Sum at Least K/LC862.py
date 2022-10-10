'''
Leetcode 862. Shortest Subarray with Sum at Least K

Description:
Given an integer array nums and an integer k, 
return the length of the shortest non-empty subarray of nums with a sum of at least k. 
If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
'''

# @param nums List[int] 
# @param k int
# @return int


'''
Refer to LC560
Prefix Sum: sum(arr[i:j]) = sum(arr[:j]) - sum(arr[:i])
'''
### Prefix + Monotonic Stack
### TC: O(n) and SC: O(n)
class Solution:
    def shortestSubarray(self, nums, k):
        prefix = [0] ### trick: padding for none prefix so that sum(arr[:i]) = prefix[i] - prefix[0]
        for n in nums:
            prefix.append(prefix[-1] + n) ### sum(arr[:i])

        ans = float("inf")
        stack = [] ### maintain an ascending stack
        for i in range(len(prefix)):
            '''
            The reason why we maintain an ascending stack is that
            if we meet a smaller but later cumulative sum(prefix), 
            it means that we will definitly use this prefix because it can form shorter subarray
            if j < i and prefix[i] <= prefix[j], i must be better than j for the current index
            since the previous numbers can not form a subarray which is larger than k,
            we can abandon them
            '''
            while stack and prefix[i] <= prefix[stack[-1]]:
                stack.pop() ### abandon the previous but larger prefix

            '''
            the first number in stack is the minimum in the stack
            if we can use the minimum to achieve the k
            the current minimum will never be used because
            for any j > cur, we have cur-i < j-i
            so we update the ans and pop the minimum from the stack
            '''
            while stack and prefix[i] - prefix[stack[0]] >= k:  
                ans = min(ans, i - stack.pop(0))

            stack.append(i)

        return ans if ans != float("inf") else -1
