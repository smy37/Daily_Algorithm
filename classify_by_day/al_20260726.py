from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_codes = ["0", "1"]

        for _ in range(n - 1):
            zero_prefixed_codes = []
            one_prefixed_codes = []

            for code in gray_codes:
                zero_prefixed_codes.append(f"0{code}")

            for code in reversed(gray_codes):
                one_prefixed_codes.append(f"1{code}")

            gray_codes = zero_prefixed_codes + one_prefixed_codes

        return [int(code, 2) for code in gray_codes]
