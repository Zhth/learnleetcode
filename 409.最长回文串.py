#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {c: s.count(c) for c in set(s)}    # 字符计数集
        return sum(count >> 1 << 1 for count in counter.values()) + \
               (1 if any(count & 1 for count in counter.values()) else 0)


        # tempDic = {}
        # for char in s:
        #     if char in tempDic:
        #         char += 1
        #     else:
        #         tempDic[char] = 1
        # flag = False
        # for char in tempDic:


# @lc code=end

