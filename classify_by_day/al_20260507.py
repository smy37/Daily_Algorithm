class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # if len(s)%2 == 0:   ## 짝수
        #     start_idx = len(s)//2
        #
        #     while start_idx > 0:
        #         hash_value_1 = 0
        #
        #         for i in range(start_idx, start_idx+start_idx):
        #             hash_value_1 += (len(s)-start_idx-1)**2*ord(s[i])
        #
        #         hash_value_2 = 0
        #
        #         for i in range(start_idx-1, -1, -1):
        #             hash_value_2 += i**2*ord(s[i])
        #         if hash_value_1 == hash_value_2:
        #             break
        #         start_idx -= 1
        #     right = s[start_idx:]
        #     return right[-1:-1:-1]+right
        # else:   ## 홀수
        #     start_idx =

        # if len(s)%2 == 0:
        #     right_idx = len(s)//2
        #     left_idx = right_idx -1
        #
        #     while right_idx > 0:
        #         hash_value_1 = 0
        #
        #         for i in range(right_idx, right_idx*2):
        #             hash_value_1 += 2**(right_idx-(i-right_idx)-1)*ord(s[i])
        #
        #         hash_value_2 = 0
        #
        #         for i in range(left_idx, -1, -1):
        #             hash_value_2 += 2**(i)*ord(s[i])
        #         print("검증", hash_value_1, hash_value_2, left_idx, right_idx, s[:left_idx+1], s[right_idx:])
        #         if hash_value_1 == hash_value_2:
        #             break
        #         right_idx -= 1
        #         left_idx = right_idx -1
        #     right = s[right_idx:]
        #     print(right, right_idx)
        #     return right[-1::-1] + right
        # else:
        #     right_idx = len(s)//2+1
        #     left_idx = len(s)//2-1
        #
        #     hash_value_1 = 0
        #
        #     for i in range(right_idx, right_idx * 2):
        #         hash_value_1 += (right_idx - (i - right_idx) - 1) ** 2 * ord(s[i])
        #
        #     hash_value_2 = 0
        #
        #     for i in range(left_idx, -1, -1):
        #         hash_value_2 += (i) ** 2 * ord(s[i])
        #
        #     if hash_value_1 == hash_value_2:
        #         return s
        #     right_idx = left_idx + 1
        #     while left_idx >=0:
        #         hash_value_1 = 0
        #
        #         for i in range(right_idx, right_idx * 2):
        #             hash_value_1 += (right_idx - (i - right_idx) - 1) ** 2 * ord(s[i])
        #
        #         hash_value_2 = 0
        #
        #         for i in range(left_idx, -1, -1):
        #             hash_value_2 += (i) ** 2 * ord(s[i])
        #
        #         if hash_value_1 == hash_value_2:
        #             break
        #         right_idx -= 1
        #         left_idx = right_idx - 1
        #     right = s[right_idx:]
        #
        #     return right[-1:-1:-1] + right

        base = 29
        forward_hash = 0
        reverse_hash = 0
        power = 1
        cri_idx = -1

        for idx, ch in enumerate(s):
            val = ord(ch)-ord('a')+1

            forward_hash = forward_hash*base+val
            reverse_hash = reverse_hash + val*power

            if forward_hash == reverse_hash:
                cri_idx = idx

            power *= base

        suffix = s[cri_idx+1:]
        return suffix[::-1] + s
sol = Solution()
print(sol.shortestPalindrome("aacecaaa"))