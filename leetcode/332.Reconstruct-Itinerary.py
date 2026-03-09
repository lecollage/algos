from collections import deque
from typing import Optional, List

# @lc code=start
class Solution:
    def getPath(self, graph, start):
        st = [start]
        path = []

        while st:
            v = st[-1] # ???

            if not graph[v]:
                st.pop()
                path.append(v)
            else:
                u = graph[v].pop()
                st.append(u)

        return path

    def findItinerary(self, edges: List[List[str]]) -> List[str]:
        graph = {}
        
        for u, v in edges:
            graph[u] = []
            graph[v] = []

        # in_deg, out_deg = {v: 0 for v in graph}, {v: 0 for v in graph}

        for _, [u, v] in enumerate(edges):
            graph[u].append(v)

        for v in graph:
            graph[v].sort(reverse=True)

        path = self.getPath(graph, 'JFK')

        path.reverse()

        return path
        #     in_deg[v] += 1
        #     out_deg[u] += 1

        # print(in_deg)
        # print(out_deg)

        # start = ''
        # finish = ''

        # for v in in_deg:
        #     if out_deg[v] == in_deg[v]:
        #         pass
        #     elif out_deg[v] == in_deg[v] + 1:
        #         if start != '':
        #             return -1

        #         start = v
        #     elif in_deg[v] == out_deg[v] + 1:
        #         if finish != '':
        #             return -1

        #         finish = v
        #     else:
        #         return -1

        # print(start, finish)

        # if start == finish == '':
        #     pass
        # elif (start == '' and finish != '') or (start != '' and finish == ''):
        #     return -1
        # elif start != 'JFK':
        #     return -1

        # fake_edge = tuple()

        # if start != '' and finish != '':
        #     if finish in graph:
        #         graph[finish].append(start)
        #     else:
        #         graph[finish] = [start]

        #     fake_edge = (finish, start)

        # for v in graph:
        #     graph[v].sort(reverse=True)

        # path = self.getPath(graph, 'JFK')

        # # if start != '' and finish != '':
        # path.reverse()

        # return path
# @lc code=end

testCases = [
   [
       [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],
       ["JFK","MUC","LHR","SFO","SJC"],
   ],
   [
       [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
       ["JFK","ATL","JFK","SFO","ATL","SFO"],
   ],
   [
       [["SFO", "JFK"], ["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
       ["JFK","ATL","JFK","SFO","ATL","SFO","JFK"],
   ],
]

for [edges,expect] in testCases:
   s = Solution()
   res = s.findItinerary(edges)

   print(res == expect, res)
   print('')
   print('')
   print('')