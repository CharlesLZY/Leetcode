'''
Leetcode 1109. Corporate Flight Bookings

Description:
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [first_i, last_i, seats_i] 
represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

Example:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:   10  10
Booking 2 reserved:       20  20
Booking 3 reserved:       25  25  25  25
Total seats:          10  55  45  25  25
Hence, answer = [10,55,45,25,25]
'''

# @param bookings List[List[int]]
# @param n int
# @return List[int]

'''
### 差分数组
差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行加减。
diff[0] = nums[0]
diff[i] = nums[i] - nums[i-1] 
The original array nums can be retrieved from difference array.

If we want to add x to nums[i:j], we only need to update diff[i] += x and diff[j] -= x
diff[i] += x equals to adding x for nums[i:]
diff[j+1] -= x equals to substracting x for nums[j:]
'''
### Difference Array Solution
### TC: O(n) and SC: O(n)
class Solution:
    def corpFlightBookings(self, bookings, n):
        diff = [0] * n
        for i, j, dx in bookings:
            diff[i-1] += dx
            diff[j] -= dx

        seats = [diff[0]]
        for d in diff[1:n]:
            seats.append(seats[-1] + d)

        return seats
