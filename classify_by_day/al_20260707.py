class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        cur = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > cur:
                answer += (prices[i]-cur)
                cur = prices[i]
            else:
                cur = prices[i]
        
        return answer
