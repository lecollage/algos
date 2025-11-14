from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=295 lang=python3
#
# 295. Find Median from Data Stream
#

# @lc code=start
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        None

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heappush(self.maxHeap, -1 * num)
            return

        if len(self.minHeap) == len(self.maxHeap):
            if num <= -1 * self.maxHeap[0]:
                heappush(self.maxHeap, -1 * num)
            else:
                heappush(self.minHeap, num)
        else:
            els = [num]

            if len(self.minHeap) > len(self.maxHeap):
                els.append(heappop(self.minHeap))
            else:
                els.append(-1 * heappop(self.maxHeap))

            els.sort()

            heappush(self.maxHeap, -1 * els[0])
            heappush(self.minHeap, els[1])
        None

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((-1 * self.maxHeap[0]) + self.minHeap[0])/2
        
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        
        return self.minHeap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

adjLists = [
    [
        [5,19,8,1],
        (5+8)/2,
    ],
    [
        [3,8,20],
        8,
    ],
    [
        [1],
        1,
    ],
    [
        [5,19,8,1,6],
        6,
    ],
    [
        [-5,-19,8,1,6],
        1,
    ],
]

for [arr, expect] in adjLists:
    s = MedianFinder()

    for el in arr:
        res = s.addNum(el)
        
    print(s.minHeap)
    print(s.maxHeap)

    res = s.findMedian()

    print(res == expect, res)
    print('')
    print('')
    print('')
