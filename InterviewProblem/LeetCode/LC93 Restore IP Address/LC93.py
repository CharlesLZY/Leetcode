'''
Leetcode 93. Restore IP Addresses

Description:
A valid IP address consists of exactly four integers separated by single dots. 
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, 
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
You are not allowed to reorder or remove any digits in s. 
You may return the valid IP addresses in any order.

Example:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''

# @param s str 
# @return List[str]

### TC: O(1) and SC: O(1)
class Solution:
    def restoreIpAddresses(self, s):
        res = []
        def valid(seg):
            if seg[0] == '0':
                return len(seg) == 1
            else:
                return int(seg) <= 255

        def DFS(i, dots): ### i: string position, dots: dot position
            nonlocal s
            if len(dots) == 4: ### dots[-1] always equals to i
                if i == len(s):
                    ip = s[:dots[0]]+'.'+s[dots[0]:dots[1]]+'.'+s[dots[1]:dots[2]]+'.'+s[dots[2]:]
                    res.append(ip)
                return
            else:
                for j in range(3):
                    if i+j < len(s):
                        if valid(s[i:i+j+1]):
                            DFS(i+j+1, dots+[i+j+1])

                            ### backtrack version
                            # dots.append(i+j+1)
                            # DFS(i+j+1, dots)
                            # dots.pop() ### backtrack
                    else:
                        break
        
        DFS(0, [])
        return res