from typing import List
from collections import deque
import copy

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        ## First Approach
        # graph = {}
        # for idx, nodes in enumerate(routes):
        #     for i in range(len(nodes)):
        #         for j in range(i+1, len(nodes)):
        #             a, b = nodes[i], nodes[j]
        #             if a not in graph:
        #                 graph[a] = {}
        #             if b not in graph:
        #                 graph[b] = {}
        #
        #             if b not in graph[a]:
        #                 graph[a][b] = set()
        #
        #             if a not in graph[b]:
        #                 graph[b][a] = set()
        #
        #             graph[a][b].add(idx)
        #             graph[b][a].add(idx)
        #
        # answer = float("inf") if source != target else 0
        # dq = deque()
        # visit = {source: True}
        # bus_list = {}
        # dq.append([source, bus_list])
        #
        # while dq:
        #     cur_source, cur_bus_list = dq.popleft()
        #
        #     if cur_source in graph:
        #         for next_source in graph[cur_source]:
        #             if next_source not in visit:
        #                 visit[next_source] = True
        #                 for bus in graph[cur_source][next_source]:
        #                     temp_list = copy.deepcopy(cur_bus_list)
        #                     temp_list[bus] = True
        #                     dq.append([next_source, temp_list])
        #                     if next_source == target:
        #                         answer = min(answer, len(temp_list.keys()))
        # if answer == float("inf"):
        #     answer = -1

        ## Second Approach
        graph = {}
        for bus_idx, stops in enumerate(routes):
            for stop in stops:
                if stop not in graph:
                    graph[stop] = {}
                graph[stop][bus_idx] = True

        answer = float("inf") if source != target else 0
        dq = deque()
        dq.append([source, 0])
        visit = {source: True}
        visit_bus = {}
        while dq:
            cur, cnt = dq.popleft()
            if cur in graph:
                for bus in graph[cur]:
                    if bus in visit_bus:
                        continue
                    visit_bus[bus] = True
                    for next_stop in routes[bus]:
                        if next_stop not in visit:
                            visit[next_stop] = True
                            dq.append([next_stop, cnt + 1])
                            if next_stop == target:
                                return cnt + 1

        return answer if answer != float("inf") else -1

if __name__ == "__main__":
    r = [[1, 2, 7], [3, 6, 7]]
    s = 1
    t = 6
    sol = Solution()
    print(sol.numBusesToDestination(r, s, t))

    explain = """
    An important property of BFS is that when a node is reached for the first time, the path used to reach that node is the shortest path. 
    """