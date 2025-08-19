from typing import List
from collections import deque

# @lc code=start
class Solution:
    def earliestFinishTime(self, landStartTimes: List[int], landDurations: List[int], waterStartTimes: List[int], waterDurations: List[int]) -> int:
        minTime = 1000000000

        landTimes = []

        for i, landStart in enumerate(landStartTimes):
            landDuration = landDurations[i]
            landEnd = landStart + landDuration
            
            landTimes.append((landStart, landDuration, landEnd))


        waterTimes = []

        for j, waterStart in enumerate(waterStartTimes):
            waterDuration = waterDurations[j]
            waterEnd = waterStart + waterDuration
            
            waterTimes.append((waterStart, waterDuration, waterEnd))

        landTimes.sort(key=lambda x: x[2])
        waterTimes.sort(key=lambda x: x[2])

        print(landTimes, waterTimes)

        minLandStart, minLandDuration, minLandEnd = landTimes[0]

        for waterStart, waterDuration, waterEnd in waterTimes:
            if waterEnd <= minLandStart:
                minTime = min(minTime, minLandEnd)
                break
            elif waterStart >= minLandEnd:
                minTime = min(minTime, waterEnd)
                break
            else:
                if minLandStart < waterStart:
                    minTime = min(minTime, minLandEnd + waterDuration)
                else:
                    minTime = min(minTime, waterEnd + minLandDuration)

        
        minWaterStart, minWaterDuration, minWaterEnd = waterTimes[0]

        for landStart, landDuration, landEnd in landTimes:
            if landEnd <= minWaterStart:
                minTime = min(minTime, minWaterEnd)
                break
            elif landStart >= minWaterEnd:
                minTime = min(minTime, landEnd)
                break
            else:
                if minWaterStart < landStart:
                    minTime = min(minTime, minWaterEnd + landDuration)
                else:
                    minTime = min(minTime, landEnd + minWaterDuration)
                   

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

