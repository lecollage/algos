from typing import List
from collections import deque


'''
Q3. Minimum Time to Activate String
You are given a string s of length n and an integer array order, where order is a permutation of the numbers in the range [0, n - 1].

Starting from time t = 0, replace the character at index order[t] in s with '*' at each time step.

A substring is valid if it contains at least one '*'.

A string is active if the total number of valid substrings is greater than or equal to k.

Return the minimum time t at which the string s becomes active. If it is impossible, return -1.

Constraints:

1 <= n == s.length <= 10**5
order.length == n
0 <= order[i] <= n - 1
s consists of lowercase English letters.
order is a permutation of integers from 0 to n - 1.
1 <= k <= 109
'''

# @lc code=start
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)

        def isActive(t: int) -> bool:
            arr = list(s)

            '''
            0..t
            order

            qwerty
            qwer*y

            6*1

            0..4 -> 5
            4..5 -> 2
            qwer*y
            wer*y
            er*y
            r*y
            *y
            qwer*
            wer*
            er*
            r*
            *

            q*er*y
            0..1 -> 2
            1..5 -> 5


            |    |
            qwerty
             |   |
            qwerty
              |  |
            qwerty
            ...
                 |
            qwerty



            ....*....*......*...

            0..*
            *..*
            *...


            0..n-1

            0: n-0
            1: n-1
            n-1: 1

            n*(a+b)/2
            n*(n+1)/2

            n * (n + 1) / 2  -> all substrings for s
            k * (k + 1) / 2  -> all substrings for non * parts
            '''

            for i in range(t+1):
                arr[order[i]] = '*'

            prevStar = -1
            sumInvalidSubstrs = 0

            for i in range(len(arr)):
                if arr[i] == "*":
                    # calc invalid substrs
                    partLen = i-prevStar-1
                    invalidSubstrs = partLen * (partLen + 1) // 2
                    sumInvalidSubstrs += invalidSubstrs
                    prevStar = i

            partLen = n-prevStar-1
            invalidSubstrs = partLen * (partLen + 1) // 2
            sumInvalidSubstrs += invalidSubstrs

            sumAll = n * (n + 1) // 2
            sumValid = sumAll-sumInvalidSubstrs

            # print(sumValid, t, sumAll, sumInvalidSubstrs)

            return sumValid >= k

        left = -1
        right = n

        while left+1 < right:
            middle = (left + right)//2

            if isActive(middle):
                right = middle
            else: 
                left = middle

        if right == n:
            return -1

        return right

# @lc code=end

'''
t - index in order arr

      l r
f f f f t t t t t t

'''

testCases = [
    {
        "s": "abc",
        "order":  [1,0,2],
        "k":  2,
        "expected": 0
    },
    {
        "s": "cat",
        "order":  [0,2,1],
        "k":  6,
        "expected": 2
    },
]

for testCase in testCases:
    print('')

    s = testCase["s"]
    order = testCase["order"]
    k = testCase["k"]
    expected = testCase["expected"]

    sol = Solution()

    result = sol.minTime(s, order, k)
    print(s, order, k, result)
    assert result == expected, f"result {result} should be expected: {expected}"

