import copy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                v = board[i][j]

                b_idx = (i//3)*3+ j//3
                if v in row[i] or v in col[j] or v in boxes[b_idx]:
                    return False

                row[i].add(v)
                col[j].add(v)
                boxes[b_idx].add(v)

        return True
                
