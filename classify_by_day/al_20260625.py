from collections import deque

class Solution():
    def solve(self, board: List[List[str]])-> None:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visit = {}
        convert_group = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visit:
                    flag = True
                    dq = deque()
                    visit[(i, j)] = True
                    dq.append((i, j))
                    temp_group = [(i, j)]

                    while dq:
                        cur_x, cur_y = dq.popleft()

                        for k in range(4):
                            nx = cur_x + dx[k]
                            ny = cur_y + dy[k]

                            if 0<= nx < len(board) and 0<= ny < len(board[0]):
                                if (nx, ny) not in visit and board[nx][ny] == "O":
                                    visit[(nx, ny)] = True
                                    dq.append((nx, ny))
                                    temp_group.append((nx, ny))
                            else:
                                flag = False
                    
                    if flag:
                        convert_group.append(temp_group)

        for group in convert_group:
            for i, j in group:
                board[i][j] = "X"
