import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {}
        self.num = n

        for s, t, w in edges:
            if s not in self.graph:
                self.graph[s] = {}
            self.graph[s][t] = w

    def addEdge(self, edge: List[int]) -> None:
        s, t, w = edge
        if s not in self.graph:
            self.graph[s] = {}
        self.graph[s][t] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        hq = [[0, node1]]
        visit = {node1: True}
        dist = [float("inf") for _ in range(self.num)]
        dist[node1] = 0
        while hq:
            cur_dist, cur_node = heapq.heappop(hq)

            if cur_node == node2:
                return cur_dist

            if cur_node in self.graph:
                for next_node in self.graph[cur_node]:
                    if next_node not in visit:
                        visit[next_node] = True
                        w = self.graph[cur_node][next_node]

                        if dist[cur_node] + w < dist[next_node]:
                            dist[next_node] = dist[cur_node] + w
                            heapq.heappush(hq, [dist[next_node], next_node])

        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)