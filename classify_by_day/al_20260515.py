class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def check_common(a, b):
            for i in range(2, a // 2 + 1):
                if a % i == 0 and b % i == 0:
                    return True
            return False

        nums = sorted(nums, reverse=True)
        group_dict = {i: i for i in nums}
        group_num = {i: 1 for i in nums}

        for i in range(len(nums)):
            n1 = nums[i]
            for j in range(i + 1, len(nums)):
                n2 = nums[j]

                if check_common(n2, n1):
                    group_dict[n2] = group_dict[n1]
                    group_num[group_dict[n1]] += 1

        return max(group_num.values())