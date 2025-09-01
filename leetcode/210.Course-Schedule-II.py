from typing import List

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph
        # visited
        # DFS

        graph = [[] for _ in range(numCourses)]

        for _, prerequisite in enumerate(prerequisites):
            if len(prerequisite) > 0:
                v,u = prerequisite
                graph[u].append(v)

        print(graph)

        result = []

        def DFS(node: int):
            if visited[node] == 1:
                return False
            
            if visited[node] == 2:
                return True

            visited[node] = 1

            for neighbour in graph[node]:
                if not DFS(neighbour):
                    return False

            visited[node] = 2
            result.append(node)

            return True

        visited = [0] * numCourses

        for node in range(numCourses):
            if visited[node] == 0 and not DFS(node):
                return []

        result.reverse()
        print(result)

        return result

        # tout.sort(key = lambda x: -x[0]) # reverse

        # print(tin)
        # print(tout)

        # result = []

        # for _, indx in tout:
        #     result.append(indx)

        # print(result)


# @lc code=end

inputs = [
    [
        2,
        [
            [1,0]
        ],
        [[0,1]]
    ],
    [
        4,
        [
            [1,0],[2,0],[3,1],[3,2]
        ],
        [[0,1,2,3], [0,2,1,3]]
    ],
    [
        1,
        [
            []
        ],
        [[0]]
    ],
    [
        4,
        [
            [1,0],[2,0],[0,2]
        ],
        [[]]
    ],
]

for n, cources, expects in inputs:
    print()
    s = Solution()
    res = s.findOrder(n, cources)

    result = False

    for expect in expects:
        result = result or expect == res

    assert result == True, f"result {res} should be in expects: {expects}"

