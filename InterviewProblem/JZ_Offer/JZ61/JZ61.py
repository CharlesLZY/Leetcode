'''
JZ61 扑克牌顺子

描述：
现在有2副扑克牌，从扑克牌中随机五张扑克牌，我们需要来判断一下是不是顺子。
有如下规则：
1. A为1，J为11，Q为12，K为13，A不能视为14
2. 大、小王为 0，0可以看作任意牌
3. 如果给出的五张牌能组成顺子（即这五张牌是连续的）就输出true，否则就输出false。
4.数据保证每组5个数字，每组最多含有4个零，数组的数取值为 [0, 13]
'''

'''
无不无聊啊
'''

# @param numbers List[int] 
# @return bool

class Solution:
    def IsContinuous(self, numbers):
        numbers.sort()
        n_zeros = 0
        ### check whether there is any duplicate (except for 0)
        for i in range(0, 4):
            if numbers[i] == 0:
                n_zeros += 1
            elif numbers[i] == numbers[i+1]:
                return False

        gap = 0
        for i in range(n_zeros+1, 5):
            gap += numbers[i] - numbers[i-1] - 1

        if gap <= n_zeros:
            return True
        else:
            return False





