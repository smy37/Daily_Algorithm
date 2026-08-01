import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        candidate = []

        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] == ".":
                    candidate.append((i, j))
                
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                    


        def dfs(b, idx):
            if idx == len(candidate):
                return True
            i, j = candidate[idx]
            cri_x = (i//3)*3
            cri_y = (j//3)*3
            temp = {str(k) : True for k in range(1, 10)}
            
            for k in range(9):
                if b[i][k] in temp:
                    del temp[b[i][k]]
                
                if b[k][j] in temp:
                    del temp[b[k][j]]

                if b[cri_x+k//3][cri_y+k%3] in temp:
                    del temp[b[cri_x+k//3][cri_y+k%3]]
            
            for k in temp:
                b_copy = copy.deepcopy(b)
                b_copy[i][j] = str(k)
                flag = dfs(b_copy, idx+1)
                if flag:
                    return True

            return False

        return dfs(board, 0)

                
