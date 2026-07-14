class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][0] = 1
        cur_x, cur_y = 0, 0
        cri = 0
        for i in range(n*n-1):
            cur_x += dx[cri]
            cur_y += dy[cri]

            board[cur_y][cur_x] = i+1

        return board
