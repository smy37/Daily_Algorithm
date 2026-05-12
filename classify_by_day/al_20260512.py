class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(n, k, stack):
            if len(stack) == k:
                answer.append(stack)
                return

            cri = stack[-1]
            for i in range(cri + 1, n + 1):
                dfs(n, k, stack + [i])

        for i in range(1, n + 1):
            dfs(n, k, [i])

        return answer
