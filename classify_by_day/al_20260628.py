from collections import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        answer = 0
        visit = {}
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dx = [1, 0]
        dy = [0, 1]
        dq = deque()
        dq.append((0, 0))
        visit[(0, 0)] = 1

        
        while dq:
            cur_x, cur_y = dq.popleft()
            
            for i in range(2):
                next_x, next_y = cur_x+dx[i], cur_y+dy[i]

                if 0<=next_x<n and 0<=next_y<m:
                    if obstacleGrid[next_x][next_y] == 1:
                        continue
                    if (next_x, next_y) not in visit:
                        visit[next_x, next_y] = 0
                        dq.append((next_x, next_y))
                    visit[next_x, next_y] += visit[cur_x, cur_y]
        if (n-1, m-1) not in visit:
            return 0
        return visit[(n-1, m-1)]
