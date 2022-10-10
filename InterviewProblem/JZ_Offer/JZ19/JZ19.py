'''
JZ19 正则表达式匹配

描述：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（包含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

'''

# @param str string 
# @param pattern string 
# @return bool

### Recursive Solution
class Solution:
    def match(self, string, pattern):

        def check(s_i, p_j):
            if p_j >= len(pattern): ### pattern is run out
                return s_i == len(string) ### if string is also run out, then the whole string is matched

            if p_j + 1 < len(pattern) and pattern[p_j+1] == '*': ### handle _* pattern
                if check(s_i, p_j+2): ### we can also skip current _* pattern
                    return True
                else: ### if skip current _* pattern will not lead to a successful match, then we have to match it
                    if s_i == len(string): ### string is run out, nothing to match, then fail
                                           ### if current _* pattern is .*, it will not fall in this trap (check(s_i, p_j+2) will succeed)
                        return False
                    else: ### we still have something to match
                        if pattern[p_j] == '.' or string[s_i] == pattern[p_j]: ### matched
                            return check(s_i+1, p_j) ### p_j stays, because next turn will keep trying to skip current _*
                        else: ### fail to match
                            return False
            else: ### with * postfix
                if s_i == len(string): ### string is run out, nothing to match
                    return False
                else:
                    if pattern[p_j] == '.' or string[s_i] == pattern[p_j]: ### matched
                        return check(s_i+1, p_j+1) ### move forward both s_i and p_j
                    else: ### fail to match
                        return False

        return check(0,0)


### DP Solution
class Solution:
    def match(self, string, pattern):
        DP_table = [[False] * (len(pattern) + 1) for _ in range(len(string) + 1)]
        ### the DP_table need to be filled from bottom to top
        DP_table[len(string)][len(pattern)] = True
        for s_i in range(len(string), -1, -1):
            for p_j in range(len(pattern)-1, -1, -1): ### starting from len(p) - 1 , DP_table[len(s)][len(p)] = True and DP_table[s_i < len(s)][len(p)] = False
                direct_match = s_i < len(string) and (pattern[p_j] == '.' or pattern[p_j] == string[s_i]) ### at first we need have string to match (s_i < len(string)?), then we consider whether the current pattern is matched
                if p_j + 1 < len(pattern) and pattern[p_j+1] == '*': ### we can skip the current _* or match it
                    ### if skip the current _* pattern, the result will depend on the successor match dp[s_i][p_j+2]
                    ### if directly match the current _* pattern, the result will depend on whether the current pattern is matched and the successor match dp[s_i+1][p_j]
                    DP_table[s_i][p_j] = DP_table[s_i][p_j+2] or (direct_match and DP_table[s_i+1][p_j])
                else: ### without * postfix, we have to match the current pattern
                    DP_table[s_i][p_j] = direct_match and DP_table[s_i+1][p_j+1] ### the result depends on whether the current pattern is matched and the successor match dp[s_i+1][p_j+1]

        return DP_table[0][0]
        