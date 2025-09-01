from typing import List
from collections import deque

# 

# @lc code=start
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        pruned = ""

        for el in s:
            if el in ['L', 'C', 'T']:
                pruned += el

        print(pruned)

        wasL = False
        wasC = False
        toRemove = set()

        for i, el in enumerate(pruned):
            if el == 'L':
                wasL = True
            if el == 'C':
                wasC = True
            if el == 'T' and not wasL and not wasC:
                toRemove.add(i)

        print(toRemove)

        pruned2 = ''

        for i, el in enumerate(pruned):
            if i not in toRemove:
                pruned2 += el

        print(pruned2)

        inserted = False

        if pruned2[0] == 'C':
            pruned2 = 'L'+pruned2
            inserted = True

        result = 0
        k = 0
        Lnum = 0
        Cnum = 0
        Tnum = 0
        nextL = -1

        while k < len(pruned2):
            print(k, pruned2[k], Lnum, Cnum, Tnum, k == len(pruned2)-1)

            if Cnum == 0 and Tnum == 0 and pruned2[k] == 'L':
                Lnum += 1
            elif Cnum > 0 and pruned2[k] == 'L':
                nextL = k
            elif Lnum > 0 and Tnum == 0 and pruned2[k] == 'C':
                Cnum += 1
            elif Lnum > 0 and Cnum > 0 and pruned2[k] == 'T':
                Tnum += 1

            if k == len(pruned2)-1:
                result += Lnum*Cnum*Tnum

                Lnum = 0
                Cnum = 0
                Tnum = 0

                if nextL != -1:
                    k = nextL

                nextL = -1

            k += 1

        return result




# @lc code=end


testCases = [
    {
        "s": "TTTTCLMXCXCTRT",
        "expected": 6
    },
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
    {
        "s": "LMXCXCTRT",
        "expected": 6
    },
    {
        "s": "CLMXCXCTRT",
        "expected": 6
    },
    {
        "s": "CLLCT",
        "expected": 4
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
