'''
Leetcode 134. Gas Station

Description:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, 
return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. 

If there exists a solution, it is guaranteed to be unique
'''

# @param gas List[int]
# @param cost List[int]
# @return int

### Brute Force Solution
### TC: O(n^2) and SC: O(1)
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        def nextStation(start):
            i = start
            while i < len(gas):
                yield i
                i += 1
            i = 0
            while i < start:
                yield i
                i += 1

        for i in range(len(gas)):
            curGas = 0
            stationIter = nextStation(i)
            for j in range(len(gas)):
                cur = next(stationIter)
                curGas = curGas + gas[cur] - cost[cur]
                if curGas < 0:
                    break
            if curGas >= 0:
                return i
        return -1

### Greedy SOlution (In this problem, if there exists a solution, it is guaranteed to be unique.)
### TC: O(n) and SC: O(1)
class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        curGas = 0
        totalGas = 0
        for i in range(len(gas)): ### One pass
            totalGas = totalGas + gas[i] - cost[i]
            curGas = curGas + gas[i] - cost[i]
            if curGas < 0:
                curGas = 0
                start = i + 1
        if totalGas >= 0:
            return start
        else:
            return -1