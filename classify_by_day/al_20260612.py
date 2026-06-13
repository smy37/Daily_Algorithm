class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        n = len(heights)

        memory = {}

        for i in range(n):
            memory[i] = [i]
            for j in range(i + 1, n):
                if heights[i] < heights[j]:
                    memory[i].append(j)

        for t1, t2 in queries:
            l_idx = min(t1, t2)
            r_idx = max(t1, t2)
            if l_idx == r_idx:
                answer.append(r_idx)
                continue
            if heights[l_idx] < heights[r_idx]:
                if len(memory[r_idx]) > 0:
                    answer.append(memory[r_idx][0])
                else:
                    answer.append(-1)
            elif heights[l_idx] == heights[r_idx]:
                if len(memory[r_idx]) > 1:
                    answer.append(memory[r_idx][1])
                else:
                    answer.append(-1)
            else:
                if len(memory[l_idx]) > 0:
                    for n in memory[l_idx]:
                        if n >= r_idx:
                            answer.append(n)
                            break
                    else:
                        answer.append(-1)
                else:
                    answer.append(-1)

        return answer

