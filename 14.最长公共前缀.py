#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = 0
        flag = True
        res = ''
        while flag:
            try:
                for s in strs:
                    if s[t] != strs[0][t]:
                        flag = False
                if flag:
                    res += strs[0][t]
                t += 1
            except:
                flag = False
        return res

        
# @lc code=end

