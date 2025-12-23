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
        cleanedUpPath = []

        for el in path:
            if len(cleanedUpPath) > 0 and el == '/' and cleanedUpPath[-1] == '/':
                continue

            cleanedUpPath.append(el)

        words = "".join(cleanedUpPath).split('/')

        # print(words)

        stack = []

        for word in words:
            if len(stack) > 0 and word == '..':
                stack.pop()
            else:
                stack.append(word)

        # print(stack)

        return "/" + "/".join(stack)
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
