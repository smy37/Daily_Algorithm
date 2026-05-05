from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        v_to_idx = {}
        for idx, v in enumerate(ratings):
            if v not in v_to_idx:
                v_to_idx[v] = []
            v_to_idx[v].append(idx)

        candy = [1] * len(ratings)

        for v in list(sorted(v_to_idx.keys())):
            for idx in v_to_idx[v]:
                if idx - 1 >= 0:
                    if ratings[idx - 1] > v:
                        candy[idx - 1] = max(candy[idx - 1], candy[idx] + 1)

                if idx + 1 < len(ratings):
                    if ratings[idx + 1] > v:
                        candy[idx + 1] = max(candy[idx] + 1, candy[idx + 1])

        return sum(candy)

