from typing import List

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(0, numCourses):
            graph[i] = set()

        # print(graph)

        for [course, prereq] in prerequisites:
            if course == prereq:
                return False
            
            graph[course].add(prereq)
            # graph[course] = graph[course].union(graph[prereq])

            visited = set()
            queue = [course]

            while len(queue) > 0:
                node = queue.pop(0)

                if node in visited:
                    continue
                
                visited.add(node)
                
                queue.extend([*graph[node]])

                # print(queue)

                if node != course:
                    graph[course] = graph[course].union(graph[node])

                if course in graph[node]:
                    return False

        # print(graph)
        return True

# @lc code=end


inputs = [
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
        ],
        True
    ],
    [
        2,
        [
            [1,0]
        ],
        True
    ],
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
            [3,0],
        ],
        True
    ],
    [
        4,
        [
            [1,0],
            [2,1],
            [2,3],
            [0,3],
            [3,0],
        ],
        False
    ],
    [
        3,
        [
            [1,0],
            [0,2],
            [2,1]
        ],
        False
    ],
    [
        4,
        [
            [3,2],
            [3,1],
            [2,0],
            [1,0],
            [0,1],
        ],
        False
    ],
    [
        9,
        [
            [3,2],
            [3,1],
            [2,0],
            [1,0],

            [4,3],

            [5,6],
            [5,7],
            [7,8],
            [6,8],
            [8,0],

            [0,5],
        ],
        False
    ]
]

for n, cources, expect in inputs:
    s = Solution()
    res = s.canFinish(n, cources)
    print(res == expect)


'''
            [1,0],
            [2,1],
            [2,3],
            [3,0],
            [0,3],

{
    0: [3]
    1: [0]
    2: [1,3]
    3: [0]
}

[
    [0,10],
    [3,18],
    [5,5],
    [6,11],
    [11,14],
    [13,1],
    [15,1],
    [17,4]
]

{
    0: [10]
    3: [18]
    5: [5]
}

[
    [1,0],
    [0,2],
    [2,1]
]

{
    0: [2]
    1: [0]
    2: [1,0]
}

'''
