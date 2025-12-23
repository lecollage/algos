from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=346 lang=python3
#
# 346. Moving Average from Data Stream
#

# @lc code=start
class MovingAverage:
    def __init__(self, size: int):
        self.maxLen = size
        self.q = deque(maxlen=self.maxLen)
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.maxLen:
            self.sum -= self.q[0]

        self.q.append(val)
        self.sum += val

        # print(self.maxLen, self.sum, val, self.q)

        return self.sum / len(self.q)
# @lc code=end

for _ in range(1):
    movingAverage = MovingAverage(3)

    print(movingAverage.next(1)) # return 1.0 = 1 / 1
    print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
    print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
    print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3
    print(movingAverage.next(-1)) # return 2.3... = (-1 + 5 + 3) / 3
    print(movingAverage.next(-10)) # return -2 = (-1 - 10 + 5) / 3
    print(movingAverage.next(-10)) # return -7 = (-1 - 10 - 10) / 3
