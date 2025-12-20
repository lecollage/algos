from typing import List, Optional

from collections import deque
#
# @lc app=leetcode id=901 lang=python3
#
# 901. Online Stock Span
#
#
# @lc code=start
class StockSpanner:
    def __init__(self):
        self.stack = [] # (index, value)
        self.index = 0

    def next(self, price: int) -> int:
        self.index += 1

        print('1', self.index, self.stack)

        while len(self.stack) > 0 and self.stack[-1][1] <= price:
            self.stack.pop()

        print('2', self.index, self.stack)

        if len(self.stack) == 0:
            self.stack.append((self.index, price))
            return self.index
        
        span = self.index - self.stack[-1][0]

        self.stack.append((self.index, price))

        return span

        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

'''
'''



s = StockSpanner()
res = []
res.append(s.next(100))
res.append(s.next(80))
res.append(s.next(60))
res.append(s.next(70))
res.append(s.next(60))
res.append(s.next(75))
res.append(s.next(85))
print(res == [1, 1, 1, 2, 1, 4, 6], res)




s1 = StockSpanner()
res = []
res.append(s1.next(31))
res.append(s1.next(41))
res.append(s1.next(48))
res.append(s1.next(59))
res.append(s1.next(79))
print(res == [1,2,3,4,5], res)



s2 = StockSpanner()
res = []
res.append(s2.next(28))
res.append(s2.next(14))
res.append(s2.next(28))
res.append(s2.next(35))
res.append(s2.next(46))
res.append(s2.next(53))
res.append(s2.next(66))
res.append(s2.next(80))
res.append(s2.next(87))
res.append(s2.next(88))
print(res == [1,1,3,4,5,6,7,8,9,10], res)





