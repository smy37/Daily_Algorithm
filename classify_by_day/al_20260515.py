from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def check_common(a, b):
            for i in range(2, a + 1):
                if a % i == 0 and b % i == 0:
                    return True
            return False

        def find(a, parent_dict):
            if a == parent_dict[a]:
                return a
            parent_dict[a] = find(parent_dict[a], parent_dict)

            return parent_dict[a]

        def union(a, b, parent_dict):
            parent_a = find(a, parent_dict)
            parent_b = find(b, parent_dict)

            if parent_a >= parent_b:
                parent_dict[parent_b] = parent_a
            else:
                parent_dict[parent_a] = parent_b

        def find_factor(n):
            factors = []
            d = 2
            while d ** 2 <= n:
                if n % d == 0:
                    factors.append(d)
                    while n % d == 0:
                        n //= d
                d += 1

            if n > 1:
                factors.append(n)

            return factors

        factor_owner = {}
        p_dict = {n: n for n in nums}
        for n in nums:
            factor_n = find_factor(n)
            for f in factor_n:
                if f in factor_owner:
                    union(n, factor_owner[f], p_dict)
                else:
                    factor_owner[f] = n

        answer = {}

        for k, v in p_dict.items():
            p_v = find(v, p_dict)
            if p_v not in answer:
                answer[p_v] = 0
            answer[p_v] += 1

        return max(answer.values())

test = [20, 50, 9, 63]
sol = Solution()
print(sol.largestComponentSize(test))
