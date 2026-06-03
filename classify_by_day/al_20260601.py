from typing import List
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = {}
        rev_graph = {}

        for s, t, w in edges:
            if s not in graph:
                graph[s] = {}
            if t not in rev_graph:
                rev_graph[t] = {}
            graph[s][t] = min(graph[s][t], w) if t in graph[s] else w
            rev_graph[t][s] = min(rev_graph[t][s], w) if s in rev_graph[t] else w

        def shortest_path(start, num, graph):
            hq = [[0, start]]
            visit = {}
            dist = [float("inf") for _ in range(num)]
            dist[start] = 0
            while hq:
                cur_dist, cur_node = heapq.heappop(hq)

                if cur_node in visit:
                    continue
                visit[cur_node] = True

                if cur_node in graph:
                    for next_node in graph[cur_node]:
                        w = graph[cur_node][next_node]

                        if dist[cur_node] + w < dist[next_node]:
                            dist[next_node] = dist[cur_node] + w
                            heapq.heappush(hq, [dist[next_node], next_node])

            return dist

        dist1 = shortest_path(src1, n, graph)
        dist2 = shortest_path(src2, n, graph)
        dist3 = shortest_path(dest, n, rev_graph)

        answer = float("inf")
        for i in range(n):
            answer = min(answer, dist1[i] + dist2[i] + dist3[i])

        return answer if answer != float("inf") else -1
