class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # answer = 0
        #
        # for i in range(len(bombs)):
        #     cnt = 0
        #     x1, y1, r1 = bombs[i]
        #     for j in range(len(bombs)):
        #         if i == j:
        #             continue
        #         x2, y2, r2 = bombs[j]
        #
        #         if (x1-x2)**2+(y1-y2)**2 <= r1**2:
        #            cnt += 1
        #
        #     answer = max(answer, cnt)
        #
        # return answer

        answer = 0
        memory = {}

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            if i not in memory:
                memory[i] = {}
            for j in range(len(bombs)):
                if i == j: continue
                x2, y2, r2 = bombs[j]

                if (x1-x2)**2 + (y1-y2)**2 <= r1**2:
                    memory[i][j] = True

        for idx in memory:
            stack = [idx]
            visit = {idx: True}

            while stack:
                cur_idx = stack.pop()

                for next_idx in memory[cur_idx]:
                    if next_idx not in visit:
                        visit[next_idx] = True
                        stack.append(next_idx)

            answer = max(answer, len(visit))

        return answer
