from typing import List
from collections import deque

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dq = deque()
        dq.append((n-1, m-1))
        dx = [0, -1]
        dy = [-1, 0]

        visit = {(n-1, m-1): True}
        health_memory = [[float("inf") for _ in range(m)] for _ in range(n)]
        answer = 1
        answer = max(1, answer - dungeon[n-1][m-1])
        health_memory[n-1][m-1] = answer

        while dq:
            cur_r, cur_c = dq.popleft()
            cur_value = health_memory[cur_r][cur_c]
            for i in range(2):
                next_r, next_c = cur_r+dx[i], cur_c+dy[i]
                if 0<=next_r<n and 0<=next_c<m:
                    next_value = dungeon[next_r][next_c]
                    if (next_r, next_c) not in visit:
                        dq.append((next_r, next_c))
                        visit[(next_r, next_c)] = True
                    temp_answer = max(1, cur_value - next_value)
                    health_memory[next_r][next_c] = min(health_memory[next_r][next_c], temp_answer)

        answer = health_memory[0][0]

        return answer


if __name__ == "__main__":
    test_case = [[0]]
    sol = Solution()
    print(sol.calculateMinimumHP(test_case))