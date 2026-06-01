class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float("inf") for _ in range(n)] for _ in range(n)]
        for s, t, w in edges:
            graph[s][t] = w
            graph[t][s] = w

        for i in range(n):
            graph[i][i] = 0

        for m in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])

        answer = -1
        min_num = float("inf")

        for i in range(n):
            cnt = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    cnt += 1
            cnt -= 1

            if cnt <= min_num:
                min_num = cnt
                answer = i

        return answer