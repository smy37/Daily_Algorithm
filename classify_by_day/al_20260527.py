from collections import deque
from typing import List

class Solution:
    def shortestAlternatingPaths(
        self,
        n: int,
        redEdges: List[List[int]],
        blueEdges: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for a, b in redEdges:
            graph[a].append((b, 0))

        for a, b in blueEdges:
            graph[a].append((b, 1))

        answer = [-1] * n
        visited = set()

        dq = deque()
        dq.append((0, 0, -1))
        visited.add((0, -1))

        while dq:
            cur, dist, prev_color = dq.popleft()

            if answer[cur] == -1:
                answer[cur] = dist

            for nxt, color in graph[cur]:
                if color != prev_color and (nxt, color) not in visited:
                    visited.add((nxt, color))
                    dq.append((nxt, dist + 1, color))

        return answer