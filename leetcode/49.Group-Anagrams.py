from typing import Optional, List


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for s in strs:
            s1 = s

            s1 = list(s1)
            s1.sort()

            print(s1)

            key = "".join(s1)
            print(key)

            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]

        print(hashMap)

        return [v for v in hashMap.values()]



# @lc code=end

'''
'''

testCases = [
    [
        ["eat","tea","tan","ate","nat","bat"],
        [["bat"],["nat","tan"],["ate","eat","tea"]]
    ],
    [
        [""],
        [""]
    ],
    [
        ["a"],
        [["a"]]
    ],
    
]

for [a, expected] in testCases:
    print('')

    s = Solution()

    result = s.groupAnagrams(a)
    print(a)
    assert result == expected, f"result {result} should be expected: {expected}"


# dsu = DSU(10)

# dsu.merge(0, 5)

# print(dsu.parents)
# print(dsu.find(5))

# dsu.merge(5, 8)
# print(dsu.parents)
# print(dsu.find(5))
# print(dsu.find(8))