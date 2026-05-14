class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ingredient = ["a", "b", "c"]
        word_l = []

        def dfs(accum_str, target):
            if len(accum_str) == target:
                word_l.append(accum_str)
                return

            for w in ingredient:
                if len(accum_str) > 0:
                    if accum_str[-1] != w:
                        dfs(accum_str + w, target)
                else:
                    dfs(accum_str + w, target)

        dfs("", n)

        if k > len(word_l):
            return ""
        else:
            return word_l[k - 1]