from typing import List
from collections import deque

#
# @lc app=leetcode id=690 lang=python3
#
# 690. Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], targetId: int) -> int:
        importances = {}
        employeesMap = {}

        for employee in employees:
            importances[employee.id] = employee.importance
            employeesMap[employee.id] = employee

        roots = set(importances.keys())

        for employee in employees:
            for v in employee.subordinates:
                roots.remove(v)

        def dfs(id: int) -> int:
            for subordinate in employeesMap[id].subordinates:
                dfs(subordinate)
                importances[id] += importances[subordinate]

        for root in roots:
            dfs(root)

        return importances[targetId]
# @lc code=end

