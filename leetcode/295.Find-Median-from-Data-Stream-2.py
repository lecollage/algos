from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=295 lang=python3
#
# 295. Find Median from Data Stream
#

[5,19,8,1,6]

maxHeap = []

heappush(maxHeap, 19)
heappush(maxHeap, 5)
heappush(maxHeap, -1)
heappush(maxHeap, -2)

print(maxHeap)
print(heappop(maxHeap))
print(maxHeap)
print(heappop(maxHeap))
print(maxHeap)