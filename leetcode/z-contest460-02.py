from typing import List
from collections import deque

# 

# @lc code=start
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        nOrig = len(s)
        s = s + '#'
        suffT = [0] * (nOrig+1)

        for i in range(nOrig-1, -1, -1):
            suffT[i] = suffT[i+1] + (s[i] == 'T')

        # print(suffT)

        countLCT = 0
        countL = 0
        countCT = 0
        countLC = 0
        anotherCountLCT = 0

        for i in range(nOrig + 1):
            ch = s[i]

            anotherCountLCT = max(anotherCountLCT, countL * suffT[i]) # position matters

            if ch == 'L':
                countL += 1
            elif ch == 'C':
                countLCT += countL * suffT[i] # i+1
                countCT += suffT[i]
                countLC += countL

        # print(countLCT)

        return countLCT + max(countCT, countLC, anotherCountLCT)




# @lc code=end


testCases = [
    {
        "s": "LMCT",
        "expected": 2
    },
    {
        "s": "LCCT",
        "expected": 4
    },
    {
        "s": "L",
        "expected": 0
    },
]

for testCase in testCases:
    print('')

    s = testCase["s"]
    expected = testCase["expected"]

    sol = Solution()

    result = sol.numOfSubsequences(s)
    print(s, result)
    assert result == expected, f"result {result} should be expected: {expected}"
