from typing import List, Optional

from collections import deque
from math import *
from heapq import *
from string import ascii_lowercase
#
# @lc app=leetcode id=126 lang=python3
#
# 126. Word Ladder II
#

# @lc code=start
class Solution:
    def getPaths(self, prevs: dict, beginWord: str, endWord: str,):
        paths = []
        q = deque([(endWord, [endWord])]) # word, path

        while(len(q) > 0):
            word, path = q.popleft()

            if word == beginWord:
                paths.append(path)
                continue

            for neighbor in prevs[word]:
                q.append((neighbor, path + [neighbor]))

        return paths

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)

        if endWord not in words:
            return []

        q = deque([(beginWord, 0)]) # node, distance
        dist = {word: float("inf") for word in wordList}
        prevs = {word: [] for word in wordList}

        prevs[beginWord] = []
        dist[beginWord] = 0

        while(len(q) > 0):
            word, distance = q.popleft()

            if word == endWord:
                break

            for i, _ in enumerate(word):
                for el in ascii_lowercase:
                    newWord = word[:i] + el + word[i+1:]

                    if el != word[i] and newWord in words:
                        if distance + 1 < dist[newWord]:
                            q.append((newWord, distance + 1))
                            dist[newWord] = distance + 1
                            prevs[newWord].append(word)
                        elif distance + 1 == dist[newWord]:
                            prevs[newWord].append(word)
        # print(prevs)

        paths = self.getPaths(prevs, beginWord, endWord)

        # print(self.paths)

        for path in paths:
            path.reverse()
            
        return paths
# @lc code=end

adjLists = [
    [
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"],
        [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    ],
    [
        "hit",
        "cog",
        ["hot","dot","dog","lot","log"],
        []
    ]
]

for [beginWord, endWord, wordList, expect] in adjLists:
    s = Solution()
    res = s.findLadders(beginWord, endWord, wordList)

    print(res == expect, res)
    print('')
    print('')
    print('')
