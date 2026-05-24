from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: {} for i in range(n)}

        for a, b in edges:
            graph[a][b] = True
            graph[b][a] = True

        visit = {}

        answer = 0
        for i in range(n):
            if i not in visit:
                dq = deque()
                dq.append(i)
                visit[i] = True
                cri = len(graph[i])
                flag = True
                cnt = 0

                while dq:
                    cur = dq.popleft()
                    for next_node in graph[cur]:
                        if next_node not in visit:
                            visit[next_node] = True
                            dq.append(next_node)
                            cnt += 1
                            if len(graph[next_node]) != cri:
                                flag = False
                if flag and cnt == cri:
                    answer += 1

        return answer