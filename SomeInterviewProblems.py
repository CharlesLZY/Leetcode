'''
计算器只支持-1操作和*2操作，初始值x和目标值y，最少通过几步可以从x到y
'''

'''
首先这题，x如果是负数y是正数，则永远不可能到达。所以这题我们假设x,y都是正数。
如果y<x，那么x只能通过-1到达y，如果y>x，那么如果y是奇数，只能通过*2-1这个操作到达，如果y是偶数只能通过*2到达。
步骤都是固定的。
'''
def minStep(x, y):
    cur = y
    step = 0
    while cur > x:
        if cur % 2 == 0:
            step += 1
            cur = cur // 2
        else:
            step += 2
            cur = cur // 2 + 1
    step += x - cur
    return step

### DP Solution
def minStep(x, y):
    DP_table = [-1]*(y+2) ### trick: if y is odd, we have to calculate DP[y+1]
    for i in range(min(x+1, y+2)): ### y can be smaller than x
        DP_table[i] = x - i

    for i in range(x+1, y+2):
        if i % 2 == 0:
            DP_table[i] = DP_table[i // 2] + 1
            if DP_table[i-1] == -1: ### update odd number
                DP_table[i-1] = DP_table[i] + 1 

    return DP_table[-2] ### DP table ends at y+1

