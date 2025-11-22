from typing import List, Optional

from collections import deque
from math import *
from heapq import *
from string import ascii_lowercase
#
# @lc app=leetcode id=127 lang=python3
#isited.add(newWord)
# 127. Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 0)]) # node, distance
        visited = set([beginWord])

        while(len(q) > 0):
            word, distance = q.popleft()

            if word == endWord:
                return distance + 1

            for i, l in enumerate(word):
                for el in ascii_lowercase:
                    newWord = word[:i] + el + word[i+1:]
                    
                    if newWord in words and newWord not in visited:
                        q.append((newWord, distance + 1))
                        visited.add(newWord)

        return 0
# @lc code=end

adjLists = [
    [
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"],
        5
    ],
    [
        "hit",
        "cog",
        ["hot","dot","dog","lot","log"],
        0
    ]
]

for [beginWord, endWord, wordList, expect] in adjLists:
    s = Solution()
    res = s.ladderLength(beginWord, endWord, wordList)

    print(res == expect, res)
    print('')
    print('')
    print('')
