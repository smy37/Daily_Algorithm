from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        if not isWater or not isWater[0]:
            return -1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        height_board = [[-1 for _ in range(len(isWater[0]))] for _ in range(len(isWater))]

        dq = deque()
        visit = {}
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    visit[(i, j)] = True
                    dq.append((i, j))
                    height_board[i][j] = 0
        
        while dq:
            r, c = dq.popleft()
            cri = height_board[r][c]

            for i in range(4):
                n_r, n_c = r+dx[i], c+dy[i]

                if 0<=n_r<len(isWater) and 0<=n_c<len(isWater[0]):
                    if (n_r, n_c) not in visit:
                        visit[(n_r, n_c)] = True
                        dq.append((n_r, n_c))
                        height_board[n_r][n_c] = cri + 1
                    
        return height_board