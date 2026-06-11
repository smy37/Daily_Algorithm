class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.size = 2 ** (math.ceil(math.log2(self.n)) + 1)
        self.tree = [0] * self.size

        for i in range(self.n):
            self.tree[self.size // 2 + i] = nums[i]

        for i in range(self.size // 2 - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.size // 2
        diff = val - self.tree[index]
        while index > 0:
            self.tree[index] += diff
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        cur_s, cur_e = left + self.size // 2, right + self.size // 2
        sum_v = 0
        while cur_s < cur_e:
            if cur_s % 2:
                sum_v += self.tree[cur_s]
                cur_s += 1
            cur_s //= 2

            if not cur_e % 2:
                sum_v += self.tree[cur_e]
                cur_e -= 1
            cur_e //= 2

        if cur_s == cur_e:
            sum_v += self.tree[cur_s]
        return sum_v

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)