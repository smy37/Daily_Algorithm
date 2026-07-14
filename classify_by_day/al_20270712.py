class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dy = [1,0,-1,0]
        dx = [0,1,0,-1]

        board = [[0 for _ in range(n)] for _ in range(n)]
        board[0][0] = 1
        cur_x, cur_y = 0, 0
        cri = 0
        cnt = 0
        while 1:
            next_x = cur_x + dx[cri]
            next_y = cur_y + dy[cri]
            
            if 0<= next_x < n and 0<=next_y<n and board[next_x][next_y] == 0:
                board[next_x][next_y] = cnt+2
                cur_x = next_x
                cur_y = next_y
                cnt += 1
            else:
                cri = (cri+1)%4
            if cnt == n*n-1:
                break

        return board
