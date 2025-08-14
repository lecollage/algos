from typing import List
from collections import deque

'''
752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Constraints:
    1 <= deadends.length <= 500
    deadends[i].length == 4
    target.length == 4
    target will not be in the list deadends.
    target and deadends[i] consist of digits only.
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        targetTuple = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))

        # print(deadendsTuples)

        q = deque()
        visited = set()

        for deadend in deadends:
            visited.add((int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])))

        if (0,0,0,0) in visited:
            return -1

        q.append([(0, 0, 0, 0), 0])
        visited.add((0, 0, 0, 0))

        # print((1,0,0,0) == (1,0,0,0))
        # print((1,0,0,0)[0] + 1, targetTuple)

        def tuple_replace(t: tuple, index: int, value) -> tuple:
            return t[:index] + (value,) + t[index+1:]

        while q:
            el, cost = q.popleft()

            # print(el, cost)

            if el == targetTuple:
                return cost
            
            for i in range(4):
                nextItemEl1 = el[i]

                if el[i] == 9:
                    nextItemEl1 = 0
                else:
                    nextItemEl1 = el[i] + 1

                nextItemEl2 = el[i]

                if el[i] == 0:
                    nextItemEl2 = 9
                else:
                    nextItemEl2 = el[i] - 1

                el1 = tuple_replace(el, i, nextItemEl1)
                el2 = tuple_replace(el, i, nextItemEl2)

                if el1 not in visited:
                    q.append([el1, cost + 1])
                    visited.add(el1)

                if el2 not in visited:
                    q.append([el2, cost + 1])
                    visited.add(el2)

        return -1

'''
'''
testCases = [
    {
        "deadends": ["0201","0101","0102","1212","2002"],
        "target": "0202",
        "expected": 6
    },
    {
        "deadends": ["8888"],
        "target": "0009",
        "expected": 1
    },
    {
        "deadends": ["8887","8889","8878","8898","8788","8988","7888","9888"],
        "target": "8888",
        "expected": -1
    },
    {
        "deadends": ["0000"],
        "target": "8888",
        "expected": -1
    },
]


for testCase in testCases:
    print()

    deadends = testCase["deadends"]
    target = testCase["target"]
    expected = testCase["expected"]

    s = Solution()
    result = s.openLock(deadends, target)
    print(deadends, target)
    assert result == expected, f"result {result} should be expected: {expected}"