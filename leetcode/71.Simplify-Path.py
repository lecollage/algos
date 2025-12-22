from typing import List, Optional

from collections import deque
from heapq import *
#
# @lc app=leetcode id=71 lang=python3
#
# 71. Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        simplifiedPath = []
        word = []
        n = len(path)
        i = 0

        while i < len(path):
            print(path[i])

            if path[i] == '/':
                while i < n and path[i] == '/':
                    i += 1

                if len(simplifiedPath) == 0:
                    simplifiedPath.append('/')
                elif i < n and len(simplifiedPath) > 0 and simplifiedPath[-1] != '/':
                    simplifiedPath.append('/')
            elif path[i] == '.':
                while i < n and path[i] != '/':
                    word.append(path[i])
                    i += 1

                print('.', word, simplifiedPath)

                if "".join(word) == '..':
                    if len(simplifiedPath) > 1:
                        simplifiedPath.pop()
                        simplifiedPath.pop()
                elif "".join(word) == '.':
                    if len(simplifiedPath) > 1:
                        simplifiedPath.pop()
                else:
                    simplifiedPath.append("".join(word))

                print('.', simplifiedPath)
            else:
                while i < n and path[i] != '/':
                    word.append(path[i])
                    i += 1

                simplifiedPath.append("".join(word))
                
            word = []

            print(simplifiedPath)

        while len(simplifiedPath) > 1 and simplifiedPath[-1] == '/':
            simplifiedPath.pop()

        return "".join(simplifiedPath)
# @lc code=end

adjLists = [
    [
        "/////home/",
        "/home",
    ],
    [
        "/////home//foo////",
        "/home/foo",
    ],

    [
        "/home/",
        "/home",
    ],
    [
        "/home//foo/",
        "/home/foo",
    ],

    [
        "/home/user/Documents/../Pictures",
        "/home/user/Pictures",
    ],
    [
        "/../",
        "/",
    ],
    [
        "/.../a/../b/c/../d/./",
        "/.../b/d",
    ],
    [
        "/a//b////c/d//././/..",
        "/a/b/c"
    ],
    [
        "/",
        "/"
    ],
    [
        "/.",
        "/"
    ],
    [
        "/..hidden",
        "/..hidden"
    ],
    [
       "/hello../world",
       "/hello../world"
    ],
    [
       "/../..ga/b/.f..d/..../e.baaeeh./.a",
       "/..ga/b/.f..d/..../e.baaeeh./.a"
    ]
]

for [path, expect] in adjLists:
    s = Solution()
    res = s.simplifyPath(path)
        
    print(res == expect, res)
    print('')
    print('')
    print('')
