class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_branch(prefix, n):
            cur = prefix
            next_prefix = prefix + 1
            steps = 0

            while cur <= n:
                steps += min(n+1, next_prefix) - cur
                cur *= 10
                next_prefix *= 10
            
            return steps

        cur = 1
        k -= 1

        while k > 0:
            steps = count_branch(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur
