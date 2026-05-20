from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}

        for a, b in edges:
            if a not in graph:
                graph[a] = {}

            if b not in graph:
                graph[b] = {}

            graph[a][b] = True
            graph[b][a] = True

        visit = {}
        s = deque()
        s.append(source)
        visit[source] = True

        while s:
            cur = s.popleft()
            if cur == destination:
                return True
            if cur in graph:
                for next_node in graph[cur]:
                    if next_node not in visit:
                        s.append(next_node)
                        visit[next_node] = True

        return False