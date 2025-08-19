from typing import List
from collections import deque

# @lc code=start
class Solution:
    def earliestFinishTime(self, landStartTimes: List[int], landDurations: List[int], waterStartTimes: List[int], waterDurations: List[int]) -> int:
        minTime = 1000000000

        for i, landStart in enumerate(landStartTimes):
            landDuration = landDurations[i]
            landEnd = landStart + landDuration

            for j, waterStart in enumerate(waterStartTimes):
                waterDuration = waterDurations[j]
                waterEnd = waterStart + waterDuration

                # commonTime = min(landStart + landDuration, waterStart + waterDuration)

                print(landStart, landEnd, waterStart, waterEnd)

                if landEnd <= waterStart:
                    minTime = min(minTime, waterEnd)
                elif landStart >= waterEnd:
                    minTime = min(minTime, landEnd)
                else:
                    if landStart < waterStart:
                        minTime = min(minTime, landEnd + waterDuration)
                    else:
                        minTime = min(minTime, waterEnd + landDuration)

        return minTime

# @lc code=end


testCases = [
    {
        "landStartTime": [2,8],
        "landDuration": [1,4],
        "waterStartTime": [6],
        "waterDuration": [3],
        "expected": 9
    },
    {
        "landStartTime": [5],
        "landDuration": [3],
        "waterStartTime": [1],
        "waterDuration": [10],
        "expected": 14
    },
]

for testCase in testCases:
    print('')

    landStartTime = testCase["landStartTime"]
    landDuration = testCase["landDuration"]
    waterStartTime = testCase["waterStartTime"]
    waterDuration = testCase["waterDuration"]
    expected = testCase["expected"]

    s = Solution()

    result = s.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
    print(landStartTime, landDuration, waterStartTime, waterDuration, result)
    assert result == expected, f"result {result} should be expected: {expected}"

