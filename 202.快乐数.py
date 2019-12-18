#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        st.add(n)
        while True:
            s = 0
            while n != 0:
                n, t = divmod(n, 10)
                s += t ** 2
            if s == 1:
                return True
            if s in st:
                return False
            st.add(s)
            n = s
        
# @lc code=end

