class Solution:
    def totalNQueens(self, n: int) -> int:
        answer = 0
        def dfs(stack):
            nonlocal answer
            if len(stack) == n:
                answer += 1
                return

            for i in range(n):
                next_row, next_col = len(stack), i
                flag = True
                for row, col in enumerate(stack):
                    if next_col == col:
                        flag = False
                        break
                    if abs(next_col-col) == abs(next_row-row):
                        flag = False
                        break
                if flag:
                    dfs(stack+[next_col])

        dfs([])

        return answer