#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = {}
        for employee in employees:
            importance[employee.id] = employee
        target = importance[id]
        res = target.importance
        stack = target.subordinates
        while stack:
            temp = []
            for peopleid in stack:
                res += importance[peopleid].importance
                temp += importance[peopleid].subordinates
            stack = temp
        return res

        
# @lc code=end

