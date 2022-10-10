'''
Leetcode 470. Implement Rand10() Using Rand7()

Description:
Given the API rand7() that generates a uniform random integer in the range [1, 7], 
write a function rand10() that generates a uniform random integer in the range [1, 10]. 
You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing.
Note that this is not an argument passed to rand10().
'''

# @return int

import random

'''
p = 40/ 49
E(# loops) = 1 * p + 2 * (1-p) * p + 3 * (1-p)^2 * p + ... 
'''
### Rejection Samping
class Solution:
    def rand10(self):
        flag = True
        while flag:
            bit_1 = random.randint(1,7)
            bit_2 = random.randint(1,7)
            idx = bit_1 + (bit_2-1) * 7 ### trick

            if idx > 40: ### (7*7 // 10) * 10
                continue
            else:
                return idx % 10 + 1


