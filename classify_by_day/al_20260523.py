from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dq = deque()
        answer = 0
        visit = {}

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        cx, cy = -1, -1
        flag = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cx = i
                    cy = j
                    flag = True
                    break
            if flag:
                break

        if (cx, cy) != (-1, -1):
            dq.append([cx, cy])
            visit[(cx, cy)] = True
            answer += 4
        del_l = {}
        while dq:
            cx, cy = dq.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:

                    if (nx, ny) not in visit:
                        visit[(nx, ny)] = True
                        dq.append([nx, ny])
                        answer += 4
                    else:
                        cal_1 = cx * len(grid[0]) + cy
                        cal_2 = nx * len(grid[0]) + ny
                        if (min(cal_1, cal_2), max(cal_1, cal_2)) not in del_l:
                            answer -= 2
                            del_l[min(cal_1, cal_2), max(cal_1, cal_2)] = True

        return answer