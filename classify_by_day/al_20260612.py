import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        hq = []
        rest = [[] for _ in range(n)]
        answer = [-1 for _ in range(len(queries))]

        for idx, [a, b] in enumerate(queries):
            if a > b:
                a, b = b, a

            if a == b:
                answer[idx] = b
            elif heights[a] < heights[b]:
                answer[idx] = b
            else:
                rest[b].append(([heights[a], idx]))

        for i in range(n):
            for height, idx in rest[i]:
                heapq.heappush(hq, [height, idx])

            while hq and hq[0][0] < heights[i]:
                _, idx = heapq.heappop(hq)
                answer[idx] = i

        return answer