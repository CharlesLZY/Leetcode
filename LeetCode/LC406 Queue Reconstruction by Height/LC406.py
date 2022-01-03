'''
Leetcode 406. Queue Reconstruction by Height

Description:
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). 
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. 
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue.
queue[0] is the person at the front of the queue.

Example:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
'''

# @param people List[List[int]]
# @return List[List[int]]

'''
sort people by descending height and ascending rank
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] -> [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

The relative position between people have the same height is fixed, which is rank-ascending order
Set higher people first because lower people will not affect them wherever the position the lower people are.
'''

### Greedy Solution
### TC: O(n^2) (insert operation can cost O(n^2), every time reconstruct list) and SC: O(n)
class Solution:
    def reconstructQueue(self, people):
        ### sort people by descending height and ascending rank 
        people.sort(key = lambda x: (-x[0], x[1])) ### x[0] is height x[1] is rank
        ans = []
        for p in people: ### people are sorted in height-descending order 
            _, rank = p
            ### all people in the array are ensured to have higher or the same height 
            ### the relative position between people and other people whose height is larger or equal is fixed
            ans.insert(rank, p) ### just insert the people according to its rank
        return ans