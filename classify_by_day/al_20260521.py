from collections import deque


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        s = deque()
        s.append([0])

        while s:
            cur_path = s.popleft()
            cur_node = cur_path[-1]

            for next_node in graph[cur_node]:
                if next_node == len(graph) - 1:
                    answer.append(cur_path + [next_node])
                else:
                    s.append(cur_path + [next_node])

        return answer