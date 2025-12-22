from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=933 lang=python3
#
# 933. Number of Recent Calls
#

# @lc code=start
class RecentCounter:
    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        # print(self.q)

        while len(self.q) > 0 and self.q[0] < t-3000:
            self.q.popleft()

        self.q.append(t)

        return len(self.q)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

for _ in range(1):
    rc = RecentCounter()

    print(rc.ping(1))
    print(rc.ping(100))
    print(rc.ping(3001))
    print(rc.ping(3002))
    print(rc.ping(3003))
    print(rc.ping(9003))
        
    print('')
    print('')
    print('')
