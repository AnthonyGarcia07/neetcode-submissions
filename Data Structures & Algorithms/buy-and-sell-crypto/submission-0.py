class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # left = buy, right=sell
        maxP = 0

        while right < len(prices):
            # profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
            
        return maxP
