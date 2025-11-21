from typing import List
from collections import deque

#
# @lc app=leetcode id=433 lang=python3
#
# 433. Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def isValidMutation(self, gene1: str, gene2: str) -> bool:
            diff = 0

            for i in range(8):
                if gene1[i] != gene2[i]:
                    diff += 1

                if diff > 1:
                    return False
            
            return diff == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        allGenes = [startGene, *bank]
        n = len(allGenes)

        print(allGenes)

        adjList = [[] for _ in allGenes]

        for i1, gene1 in enumerate(allGenes):
            for i2 in range(i1, len(allGenes)):
                gene2 = allGenes[i2]

                if gene1 != gene2 and self.isValidMutation(gene1, gene2):
                    adjList[i1].append(i2)
                    adjList[i2].append(i1)

        print(adjList)

        queue = deque([(0, 0)]) # node, distance
        visited = [False]*n

        while(len(queue) > 0):
            node, distance = queue.popleft()

            if allGenes[node] == endGene:
                return distance 

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    queue.append((neighbour, distance + 1))
                    visited[neighbour] = True

        return -1

# @lc code=end
testCases = [
    [
        "AACCGGTT",
        "AACCGGTA",
        ["AACCGGTA"],
        1
    ],
    [
        "AACCGGTT",
        "AAACGGTA",
        ["AACCGGTA","AACCGCTA","AAACGGTA"],
        2
    ],
]

for startGene, endGene, bank, expected  in testCases:
    print(startGene, endGene, bank, expected)

    s = Solution()
    result = s.minMutation(startGene, endGene, bank)

    assert result == expected, f"result {result} should be expected: {expected}"

    print('')
    print('')
    print('')