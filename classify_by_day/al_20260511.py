class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ## First Approach
        # cur = "0"
        #
        # for _ in range(n):
        #     reverse = "".join('1' if cur[idx] == "0" else "0" for idx in range(len(cur)-1,-1,-1))
        #     cur = cur + "1" + reverse
        # return cur[k - 1]

        ## Second Approach
        if n == 1:
            return "0"

        length = (2**n)-1
        mid = (length//2)+1

        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n-1, k)
        elif k > mid:
            recur =  self.findKthBit(n-1, length-k+1)
            return "1" if recur == "0" else "0"



