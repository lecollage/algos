from typing import List, Optional

from collections import deque
import heapq
#
# @lc app=leetcode id=703 lang=python3
#
# 703. Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-1 * num for num in nums]
        self.heap1 = []
        self.heap2 = []

        heapq.heapify(self.heap)

        print(k, self.heap, range(0, k-1), range(k-1, len(nums)))

        for _ in range(0, min(k-1, len(nums))):
            x = heapq.heappop(self.heap)
            print(1, self.heap1, self.heap)
            heapq.heappush(self.heap1, -1 * x)

        while len(self.heap) > 0:
            x = heapq.heappop(self.heap)
            print(1, self.heap2, self.heap)
            heapq.heappush(self.heap2, x)

        print(self.heap1)
        print(self.heap2)
        print()

    def add(self, val: int) -> int:
        print(val, 'before', self.heap1)
        print(val, 'before', self.heap2)
        print(val, 'before', self.heap1[0], -1 * self.heap2[0])

        if len(self.heap1) == 0 or val > self.heap1[0]:
            heapq.heappush(self.heap1, val)
        elif len(self.heap2) == 0 or val >= -1 * self.heap2[0] or self.k-1 == 0:
            heapq.heappush(self.heap2, -1 * val)

        if len(self.heap1) >= self.k:
            heapq.heappush(self.heap2, -1 * heapq.heappop(self.heap1))
        
        print(val, 'after', self.heap1)
        print(val, 'after', self.heap2)

        return -1 * self.heap2[0] if len(self.heap2) > 0 else self.heap1[0]
# @lc code=end

# for _ in range(1):
#     kthLargest = KthLargest(3, [4, 5, 8, 2])
#     print(kthLargest.add(3)) # return 4
#     print(kthLargest.add(5)) # return 5
#     print(kthLargest.add(10)) # return 5
#     print(kthLargest.add(9)) # return 8
#     print(kthLargest.add(4)) # return 8

'''
4, 5, 8, 2

8, 5, 4, 2 -> 4
8, 5, 4, 3, 2 -> 4
8, 5, 5, 4, 3, 2 -> 5
10, 8, 5, 5, 4, 3, 2 -> 5
10, 9, 8, 5, 5, 4, 3, 2 -> 8
10, 9, 8, 5, 5, 4, 4, 3, 2 -> 8
'''

# print()
# print()
# print()

# for _ in range(1):
#     kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])
#     print(kthLargest.add(2)) # return 7
#     print(kthLargest.add(10)) # return 7
#     print(kthLargest.add(9)) # return 7
#     print(kthLargest.add(9)) # return 8



# kthLargest = KthLargest(3, [4, 5, 8, 2])
# print(kthLargest.add(1)) # return 4
# print(kthLargest.add(0)) # return 4
# print(kthLargest.add(3)) # return 4
# print(kthLargest.add(5)) # return 5
# print(kthLargest.add(10)) # return 5
# print(kthLargest.add(9)) # return 8
# print(kthLargest.add(4)) # return 8



[[1,[]],[-3],[-2],[-4],[0],[4]]

# kthLargest = KthLargest(1, [])
# print(kthLargest.add(-3)) # return 
# print(kthLargest.add(-2)) # return 
# print(kthLargest.add(-4)) # return 
# print(kthLargest.add(0)) # return 
# print(kthLargest.add(4)) # return 


[[3,[5,-1]],[2],[1],[-1],[3],[4]]



# kthLargest = KthLargest(3, [5,-1])
# print(kthLargest.add(2))
# print()
# print(kthLargest.add(1))
# print()
# print(kthLargest.add(-1))
# print()
# print(kthLargest.add(3))
# print()
# print(kthLargest.add(4))
# print()

'''
-1 2 5
-1 2 5



'''

# [[3, [-1, -2, -3, -4, -5]], [-6], [-7], [-8], [-9]]
# kthLargest = KthLargest(3, [-1, -2, -3, -4, -5])
# print(kthLargest.add(-6)) # return 
# print(kthLargest.add(-7)) # return 
# print(kthLargest.add(-8)) # return 
# print(kthLargest.add(-9)) # return 

# '''

# -5 -4 -3 -2 -1 
# '''


[[1,[]], [1], [2], [3], [4], [5]]

# kthLargest = KthLargest(1,[])
# print(kthLargest.add(1)) # return 
# print(kthLargest.add(2)) # return 
# print(kthLargest.add(3)) # return 
# print(kthLargest.add(4)) # return 
# print(kthLargest.add(5)) # return 

'''
1,2,3,4,5

'''

[[5, [1, 2, 3, 4, 5]], [6], [7], [8], [9]]

# kthLargest = KthLargest(5, [1, 2, 3, 4, 5])
# print(kthLargest.add(6)) # return 
# print(kthLargest.add(7)) # return 
# print(kthLargest.add(8)) # return 
# print(kthLargest.add(9)) # return 

'''
5 4 3 2 1
'''


[[4, [10000, -9999, 9998, -9997]], [9996], [-9995], [9994], [-9993], [9992], [-9991]]

kthLargest = KthLargest(4, [10000, -9999, 9998, -9997])
print(kthLargest.add(9996))
print(kthLargest.add(-9995))
print(kthLargest.add(9994))
print(kthLargest.add(-9993))
print(kthLargest.add(9992))
print(kthLargest.add(-9991))

'''
10000 9998 -9997 -9999

'''




[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

[[5, [-10000, 10000, 0, 5000, -5000]], [-10000], [10000], [-9999], [9999]]