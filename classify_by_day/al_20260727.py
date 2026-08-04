from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        candidate = []

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candidate.append((i, j))
                else:
                    num = board[i][j]
                    box_idx = (i // 3) * 3 + j // 3

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_idx].add(num)

        def dfs(idx):
            if idx == len(candidate):
                return True

            cur_i, cur_j = candidate[idx]
            box_idx = (cur_i // 3) * 3 + cur_j // 3

            for num_int in range(1, 10):
                num = str(num_int)

                if (
                    num in rows[cur_i]
                    or num in cols[cur_j]
                    or num in boxes[box_idx]
                ):
                    continue

                board[cur_i][cur_j] = num
                rows[cur_i].add(num)
                cols[cur_j].add(num)
                boxes[box_idx].add(num)

                if dfs(idx + 1):
                    return True

                board[cur_i][cur_j] = "."
                rows[cur_i].remove(num)
                cols[cur_j].remove(num)
                boxes[box_idx].remove(num)

            return False

        dfs(0)
