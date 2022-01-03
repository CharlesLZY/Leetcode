'''
Leetcode 11. Container With Most Water

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

# @param height List[int]
# @return int

### Two Pointer Solution
### TC: O(n) and SC: O(1)
class Solution:
    def maxArea(self, height):
        lp = 0
        rp = len(height) - 1
        MAX = 0
        while lp < rp:
            MAX = max(MAX, (rp-lp)*min(height[lp], height[rp]))
            if height[lp] > height[rp]:
                rp -= 1
            else:
                lp += 1

        return MAX