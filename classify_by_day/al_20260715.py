class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        answer = False
        if sorted(s1+s2) != sorted(s3):
            return False
        visit = {}
        def dfs(idx_1, idx_2, idx_3):
            if idx_3 == len(s3):
                answer = True
                return True
            if idx_1 < len(s1) and s1[idx_1] == s3[idx_3]:
                if (idx_1+1, idx_2, idx_3+1) not in visit:
                    visit[(idx_1+1, idx_2, idx_3+1)] = True
                    flag = dfs(idx_1+1, idx_2, idx_3+1)

                    if flag:
                        return True
            if idx_2 < len(s2) and s2[idx_2] == s3[idx_3]:
                if (idx_1, idx_2+1, idx_3+1) not in visit:
                    visit[(idx_1, idx_2+1, idx_3+1)] = True
                    flag = dfs(idx_1, idx_2+1, idx_3+1)
                    if flag:
                        return True

        answer = dfs(0, 0, 0)
        if answer is None:
            answer = False

        return answer
