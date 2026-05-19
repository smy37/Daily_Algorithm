from typing import List
import copy
from collections import deque


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = {}
        for a, b, t in edges:
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[a][b] = t
            graph[b][a] = t

        stack = deque([[0, maxTime, {0: values[0]}]])
        answer = 0
        while stack:
            cur_idx, cur_rest, cur_sum = stack.popleft()

            if cur_idx == 0:
                answer = max(sum(cur_sum.values()), answer)

            if cur_idx in graph:
                for next_idx in graph[cur_idx]:
                    next_value = graph[cur_idx][next_idx]

                    if cur_rest - next_value >= 0:
                        temp_dict = copy.deepcopy(cur_sum)
                        temp_dict[next_idx] = values[next_idx]
                        stack.append([next_idx, cur_rest - next_value, temp_dict])

        return answer