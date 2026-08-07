class Solution:
    def numTrees(self, n: int) -> int:
        num_list = [i for i in range(1, n+1)]
        memo = {1: 1}

        def make_tree(n_list):
            if len(n_list) in memo:
                return memo[len(n_list)]

            cur_cnt = 0

            for i in range(len(n_list)):
                left = n_list[:i]
                right = n_list[i+1:]
                left_cnt = 1
                right_cnt = 1

                if left:
                    left_cnt = make_tree(left)

                if right:
                    right_cnt = make_tree(right)
                cur_cnt += left_cnt*right_cnt
            memo[len(n_list)] = cur_cnt
            return cur_cnt

        return make_tree(num_list)
