class Solution:
    def findKthNumber(self, n: int, k: int) -> str:
        num_list = [str(i) for i in range(1, n+1)]
        num_list.sort()
        return num_list[k-1]
