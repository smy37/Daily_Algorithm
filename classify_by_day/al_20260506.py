from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        ## First Approach
        # v_to_idx = {}
        # for idx, v in enumerate(ratings):
        #     if v not in v_to_idx:
        #         v_to_idx[v] = []
        #     v_to_idx[v].append(idx)
        #
        # candy = [1] * len(ratings)
        #
        # for v in list(sorted(v_to_idx.keys())):
        #     for idx in v_to_idx[v]:
        #         if idx - 1 >= 0:
        #             if ratings[idx - 1] > v:
        #                 candy[idx - 1] = max(candy[idx - 1], candy[idx] + 1)
        #
        #         if idx + 1 < len(ratings):
        #             if ratings[idx + 1] > v:
        #                 candy[idx + 1] = max(candy[idx] + 1, candy[idx + 1])
        #
        # return sum(candy)

        candy_l = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                candy_l[i] = candy_l[i-1]+1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_l[i] = max(candy_l[i], candy_l[i+1]+1)

        return sum(candy_l)

