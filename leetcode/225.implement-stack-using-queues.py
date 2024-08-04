#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        initialLen = len(self.queue)

        for j in range(0, len(self.queue)-1):
            self.queue.append(self.queue[j])

        val = self.queue[initialLen-1]
        # print(self.queue, val)

        self.queue = self.queue[initialLen:]
        # print(self.queue)

        return val
        
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

s = MyStack()
print(s.empty())
s.push(1)
s.push(2)
s.push(3)

print(s.top())
print(s.empty())
print(s.pop())

s.push(5)
print(s.top())
print(s.pop())

s.push(10)
print(s.pop())


# #############
# s.push(1)
# print(s.pop())
# print(s.empty())
