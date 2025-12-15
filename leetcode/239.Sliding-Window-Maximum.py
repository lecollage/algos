from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=239 lang=python3
#
# 239. Sliding Window Maximum
#

# @lc code=start
class MyStack:
    def __init__(self):
        self.arr = [(0, float('-inf'))]

    def push(self, el: int):
        _, currMax = self.arr[-1]
        
        self.arr.append((el, max(currMax, el)))

    def pop(self) -> int:
        return self.arr.pop()[0]

    def getMax(self):
        _, currMax = self.arr[-1]

        return currMax
    
    def length(self):
        return len(self.arr) - 1
    
    def isEmpty(self):
        return len(self.arr) <= 1
    

class MyQueue:
    def __init__(self):
        self.stackHead = MyStack()
        self.stackTail = MyStack()

    def _move(self):
        while not self.stackTail.isEmpty():
            self.stackHead.push(self.stackTail.pop())

    def push(self, el: int):
        self.stackTail.push(el)

    def pop(self):
        if self.stackHead.isEmpty():
            self._move()

        return self.stackHead.pop()
            
    def getMax(self):
        if self.stackHead.isEmpty():
            self._move()

        return max(self.stackHead.getMax(), self.stackTail.getMax())

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        answer = []

        q = MyQueue()

        for i in range(k): # 0..k-1
            q.push(nums[i])

        answer.append(q.getMax())

        for i in range(k, n): # k..n-1
            q.pop()
            q.push(nums[i])
            answer.append(q.getMax())

        return answer
# @lc code=end

adjLists = [
    [
        [1,3,-1,-3,5,3,6,7],
        3,
        [3,3,5,5,6,7]
    ],
    [
        [1],
        1,
        [1]
    ],
    [
        [1,-1],
        1,
        [1,-1]
    ],
    [
        [7,2,4],
        2,
        [7,7]
    ],
    
]

for [nums, k, expect] in adjLists:
    s = Solution()
    res = s.maxSlidingWindow(nums, k)
    print(res == expect, res)
    print('')
    print('')
    print('')
