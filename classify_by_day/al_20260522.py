from collections import deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ## First Approach
        graph = {}

        for a, b, w in roads:
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = w
            graph[b][a] = w

        answer_candidate = []
        visit = {}
        dq = deque()
        dq.append(1)

        while dq:
            cur_node = dq.popleft()

            if cur_node in graph:
                for next_node in graph[cur_node]:
                    hash_v = (min(cur_node, next_node), max(cur_node, next_node))

                    if hash_v not in visit:
                        visit[hash_v] = True
                        answer_candidate.append(graph[cur_node][next_node])
                        dq.append(next_node)

        return min(answer_candidate)

        ## Fast Approach
        # graph = {}
        #
        # for a, b, w in roads:
        #     if a not in graph:
        #         graph[a] = {}
        #     if b not in graph:
        #         graph[b] = {}
        #     graph[a][b] = w
        #     graph[b][a] = w
        #
        # answer = float("inf")
        # visit = {1: True}
        # dq = deque()
        # dq.append(1)
        #
        # while dq:
        #     cur_node = dq.popleft()
        #
        #     if cur_node in graph:
        #         for next_node in graph[cur_node]:
        #             answer = min(answer, graph[cur_node][next_node])
        #             if next_node not in visit:
        #                 visit[next_node] = True
        #
        #                 dq.append(next_node)
        #
        # return answer