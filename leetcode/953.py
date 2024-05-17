from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashOrder = {}

        for i, el in enumerate(order):
            hashOrder[el] = i

        # print(hashOrder)

        for i in range(0, 20):
            max = -1
            onlyIncrease = True
            for word in words:
                el = -1

                if i < len(word):
                    el = hashOrder[word[i]]

                if el > max:
                    max = el
                elif el == max:
                    onlyIncrease = False
                elif el < max:
                    return False
                
            if onlyIncrease:
                return True

        return True


inputs = [
    [
        ["hello","leetcode"], 
        "hlabcdefgijkmnopqrstuvwxyz",
        True,
    ],
    [
        ["word","world","row"],
        "worldabcefghijkmnpqstuvxyz",
        False,
    ],
    [
        ["apple","app"], 
        "abcdefghijklmnopqrstuvwxyz",
        False,
    ],
    [
        ["a"], 
        "abcdefghijklmnopqrstuvwxyz",
        True,
    ],
    [
        ["a", "b"], 
        "abcdefghijklmnopqrstuvwxyz",
        True,
    ],
    [
        ["b", "a"], 
        "abcdefghijklmnopqrstuvwxyz",
        False,
    ],
]


for _, input in enumerate(inputs):
    solution = Solution()
    res = solution.isAlienSorted(input[0], input[1])
    print(res == input[2])

'''
["hello","leetcode"], 

0: 0,1
1: 6,6
2: 1,6
3: 1,19
4: 14,4

h l
e e
l e
l t
o c

leetcode


h 0
l 1
a 2
b 3
c 4
d 5
e 6
f 7
g 8
i 9
j 10
k 11
m 12
n 13
o 14
pqrstuvwxyz






["word","world","row"],
[0,0,2],

w 0
o 1
r 2
l 3
d 4

0: 0, 0, 2
1: 1, 1, 1
2: 2, 2, 0

j >= j+n



abcefghijkmnpqstuvxyz
-------------------------------



["hello","leetcode"],

0: 0, 1
1: 6, 6
2: 1, 6
3: 1, 13



h 0
l 1
a 2
b 3
c 4
d 5
e 6
fgijkmnopqrstuvwxyz


'''













