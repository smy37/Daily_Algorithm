class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # dp = [[[0, 0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # if matrix[0][0] == "1":
        #     dp[0][0] = [1, 1]
        #
        # answer = dp[0][0][0] * dp[0][0][1]
        #
        # for i in range(1, len(matrix)):
        #     if matrix[i][0] == "1":
        #         dp[i][0][0] = dp[i - 1][0][0] + 1
        #         dp[i][0][1] = 1
        #     answer = max(answer, dp[i][0][0] * dp[i][0][1])
        #
        # for i in range(1, len(matrix[0])):
        #     if matrix[0][i] == "1":
        #         dp[0][i][1] = dp[0][i - 1][1] + 1
        #         dp[0][i][0] = 1
        #     answer = max(answer, dp[0][i][0] * dp[0][i][1])
        #
        # for i in range(1, len(matrix)):
        #     for j in range(1, len(matrix[0])):
        #         if matrix[i][j] == "1":
        #             dp[i][j][0] = min(dp[i - 1][j][0], dp[i - 1][j - 1][0]) + 1
        #             dp[i][j][1] = min(dp[i][j - 1][1], dp[i - 1][j - 1][1]) + 1
        #
        #         answer = max(answer, dp[i][j][0] * dp[i][j][1])

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i - 1][j] + 1

        answer = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    h = dp[i][j]
                    temp_max = 0
                    for k in range(j, -1, -1):
                        if matrix[i][k] == "0":
                            break
                        h = min(h, dp[i][k])
                        temp_max = max(temp_max, (j - k + 1) * h)

                    answer = max(answer, temp_max)

        return answer