#
# @lc app=leetcode.cn id=756 lang=python3
#
# [756] 金字塔转换矩阵
#

# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        #将allowed进行哈希映射
        #allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"] 
        #hashmap  = {'XX': ['X', 'Y'], 'XY': ['X', 'Y'], 'YX': ['Z']})
        from collections import defaultdict
        tree = defaultdict(list)
        for s in allowed:
            tree[s[0:2]].append(s[2])
        return self.work(bottom, tree, 0)
    def work(self, bottom, tree, pos):
        if pos == len(bottom) - 1:
            pos = 0
            bottom = bottom[:-1]
        if len(bottom) <= 1:
            return True
        if bottom[pos:pos+2] not in tree.keys():
            return False
        for value in tree[bottom[pos:pos+2]]:
            btm = bottom[:pos] + value + bottom[pos+1:]
            if self.work(btm, tree, pos + 1):
                return True
        return False

        # if len(bottom) <= 1:
        #     return True
        # bottoms = [bottom]
        # rules = {}
        # for rule in allowed:
        #     trule = rule[:2]
        #     if trule in rules:
        #         rules[trule].append(rule[2])
        #     else:
        #         rules[trule] = [rule[2]]
        # while len(bottoms[0]) > 1:
        #     l = len(bottoms[0])
        #     tempbottoms = []
        #     for bottom in bottoms:
        #         flag = True
        #         tempbottom = ['']
        #         for i in range(l - 1):
        #             t = rules.get(bottom[i:i+2])
        #             if t is not None:
        #                 temp = []
        #                 for rule in t:
        #                     for tb in tempbottom:
        #                         temp.append(tb + rule)
        #                 tempbottom = temp
        #             else:
        #                 flag = False
        #                 break
        #         if flag:
        #             tempbottoms += tempbottom
        #     bottoms = tempbottoms
        #     if len(bottoms) == 0:
        #         return False
        # return True



        
            

        
# @lc code=end

