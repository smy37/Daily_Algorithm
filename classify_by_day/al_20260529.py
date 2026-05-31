class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ## Fisrt Approach
        # answer = {i + 1: float("inf") for i in range(n)}
        #
        # graph = {}
        # for u, v, w in times:
        #     if u not in graph:
        #         graph[u] = {}
        #
        #     graph[u][v] = w
        #
        # def dfs(stack, visit, dist):
        #     cur = stack.pop()
        #
        #     if cur in graph:
        #         for next_node in graph[cur]:
        #             w = graph[cur][next_node]
        #             answer[next_node] = min(answer[next_node], dist + w)
        #             if next_node not in visit:
        #                 visit[next_node] = True
        #                 dfs(stack + [next_node], visit, dist + w)
        #                 # del visit[next_node]
        #
        # s = [k]
        # v = {k: True}
        # answer[k] = 0
        #
        # dfs(s, v, 0)
        #
        # min_time = max(answer.values())
        #
        # return min_time if min_time != float('inf') else -1


        ## Second Approach
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = {}

            graph[u][v] = w

        dist = {i + 1: float("inf") for i in range(n)}
        dist[k] = 0
        s = [[0, k]]
        visit = {}

        while s:
            _, cur = heapq.heappop(s)
            if cur in visit:
                continue
            visit[cur] = True

            if cur in graph:
                for next_node in graph[cur]:
                    w = graph[cur][next_node]

                    if dist[cur] + w < dist[next_node]:
                        dist[next_node] = dist[cur] + w
                        heapq.heappush(s, [dist[next_node], next_node])

        min_time = max(dist.values())

        return min_time if min_time != float("inf") else -1