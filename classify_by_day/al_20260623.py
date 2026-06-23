class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ## First Approach
        # global answer
        # answer = float("inf")
        # visit = {}
        # def dfs(cur_row, cur_col, cur_sum):
        #     global answer
        #     if cur_row+1 < len(triangle):
        #         if (cur_row+1, cur_col, triangle[cur_row+1][cur_col]+cur_sum) not in visit:
        #             visit[(cur_row+1, cur_col, triangle[cur_row+1][cur_col]+cur_sum)] = True
        #             dfs(cur_row+1, cur_col, triangle[cur_row+1][cur_col]+cur_sum)
        #         if (cur_row+1, cur_col+1, triangle[cur_row+1][cur_col+1]+cur_sum) not in visit:
        #             visit[(cur_row+1, cur_col+1, triangle[cur_row+1][cur_col+1]+cur_sum)] = True
        #             dfs(cur_row+1, cur_col+1, triangle[cur_row+1][cur_col+1]+cur_sum)
        #     else:
        #         answer = min(answer, cur_sum)
        # visit[(0,0, triangle[0][0])] = True
        # dfs(0,0, triangle[0][0])

        # return answer

        ## Second Approach
        memory = {}

        def dfs(cur_row, cur_col):
            if cur_row == len(triangle)-1:
                return triangle[cur_row][cur_col]

            if (cur_row, cur_col) in memory:
                return memory[(cur_row, cur_col)]
            memory[(cur_row, cur_col)] = triangle[cur_row][cur_col] + min(dfs(cur_row+1, cur_col), dfs(cur_row+1, cur_col+1))

            return memory[(cur_row, cur_col)]

        answer = dfs(0, 0)
        return answer
