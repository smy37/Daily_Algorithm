class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        answer = []

        def dfs(cur_idx, dot_num, str_list):
            if dot_num == 3:
                if len(s) - cur_idx <= 3:
                    answer.append(".".join(str_list))
            if cur_idx == len(s) - 1 or len(str_list) >= 4 or dot_num >= 4:
                return
            if len(str_list[-1]) == 3:
                dfs(cur_idx + 1, dot_num + 1, str_list + [s[cur_idx]])
            else:

                dfs(cur_idx + 1, dot_num + 1, str_list + [s[cur_idx]])

                ori_num = int(str_list[-1])
                str_list[-1] = str_list[-1] + s[cur_idx + 1]
                after_num = int(str_list[-1])

                if ori_num != after_num and (0 <= after_num <= 255):
                    dfs(cur_idx + 1, dot_num, str_list)
                str_list[-1] = str_list[-1][:-1]

        dfs(0, 0, [s[0]])
        return answer