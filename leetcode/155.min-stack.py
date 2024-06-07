#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    stack = []
    minStack = []

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.minStack) == 0:
            self.minStack.append(val)
        elif self.minStack[-1] >= val:
            self.minStack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()

        if len(self.minStack) > 0 and val == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        
        return None

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

# minStack = MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# print(minStack.getMin()); # return -3
# minStack.pop();
# print(minStack.top());    # return 0
# print(minStack.getMin()); # return -2

# minStack = MinStack();
# minStack.push(-9);
# minStack.push(-14);
# minStack.push(1);
# minStack.push(-20);
# minStack.push(10);
# minStack.push(-15);
# print(minStack.getMin()); # return -20
# minStack.pop();
# print(minStack.top());    # return 10
# print(minStack.getMin()); # return -20
# minStack.pop();
# minStack.pop();
# print(minStack.getMin()); # return -14
# minStack.push(-30);
# print(minStack.getMin()); # return -30

# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]

minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print(minStack.getMin()); # return 0
minStack.pop();
print(minStack.getMin()); # return 0

'''
-15
10
-20
1
-14
-9







-20
-14
-9


'''