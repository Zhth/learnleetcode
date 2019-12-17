#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        for i in range(len(words) - 1, -1, -1):
            if words[i] != '':
                return len(words[i])
        return 0
        
# @lc code=end

