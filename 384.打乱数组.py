#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original = list(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original
        self.original = list(self.original)
        return self.array
   

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        l = len(self.array)
        for idx in range(l):
            swap_idx = random.randrange(idx, l)
            self.array[idx], self.array[swap_idx] = self.array[swap_idx], self.array[idx]

        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

