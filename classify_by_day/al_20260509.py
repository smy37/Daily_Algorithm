class Solution:
    def sumScores(self, s: str) -> int:
        # answer = 0
        #
        # forward_hash = 0
        # reverse_hash = 0
        #
        # base = 29
        # mod = 10**9 + 7
        # power = 1
        #
        # front_memory = {}
        # memory = {}
        #
        # for i in range(len(s)):
        #     front_val = ord(s[i]) - ord("a") + 1
        #     back_val = ord(s[len(s) - i - 1]) - ord("a") + 1
        #
        #     forward_hash = (forward_hash * base + front_val) % mod
        #     reverse_hash = (power * back_val + reverse_hash) % mod
        #
        #     front_memory[i + 1] = forward_hash
        #
        #     if forward_hash == reverse_hash:
        #         answer += i + 1
        #         power = (power * base) % mod
        #         memory[i] = reverse_hash
        #         continue
        #
        #     for j in range(i):
        #         length = i - j
        #
        #         temp = (reverse_hash - memory[j]) % mod
        #         temp = temp * pow(pow(base, j + 1, mod), mod - 2, mod) % mod
        #
        #         if front_memory.get(length) == temp:
        #             answer += length
        #             break
        #
        #     power = (power * base) % mod
        #     memory[i] = reverse_hash
        #
        # return answer

        answer = 0
        z_l = [0] * len(s)
        z_l[0] = len(s)
        L, R = 0, 0
        for idx in range(1, len(s)):

            if idx <= R:
                z_l[idx] = min(R - idx + 1, z_l[idx - L])

            while idx + z_l[idx] < len(s) and s[z_l[idx]] == s[idx + z_l[idx]]:
                z_l[idx] += 1

            if idx + z_l[idx] - 1 > R:
                L = idx
                R = idx + z_l[idx] - 1

        return sum(z_l) 