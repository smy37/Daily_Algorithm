`from typing import List
from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = {}
        for idx, nodes in enumerate(routes):
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    a, b = nodes[i], nodes[j]
                    if a not in graph:
                        graph[a] = {}
                    if b not in graph:
                        graph[b] = {}

                    if b not in graph[a]:
                        graph[a][b] = set()

                    if a not in graph[b]:
                        graph[b][a] = set()

                    graph[a][b].add(idx)
                    graph[b][a].add(idx)

        dq = deque()
        visit = {source: True}
        bus_list = set()




if __name__ == "__main__":
    r = [[1, 2, 7], [3, 6, 7]]
    s = 1
    t = 6
    sol = Solution()
    sol.numBusesToDestination(r, s, t)`
