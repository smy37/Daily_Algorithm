from typing import List

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = []
        count = 0

        numbers = [i for i in range(1, n + 1)]
        visited = {}

        def dfs(permutation: List[int]) -> bool:
            nonlocal count
            nonlocal answer

            if len(permutation) == n:
                count += 1

                if count == k:
                    answer = permutation[:]
                    return True

                return False

            for number in numbers:
                if number in visited:
                    continue

                visited[number] = True
                permutation.append(number)

                if dfs(permutation):
                    return True

                permutation.pop()
                del visited[number]

            return False

        dfs([])

        return "".join(map(str, answer))
