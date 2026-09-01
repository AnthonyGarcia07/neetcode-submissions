class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        maxProfit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit

# We move through the array once while keeping track of the lowest price we've seen so far. For each day, we calculate the profit we'd make by selling at the current price after buying at that lowest previous price. We keep the maximum of those profits. Since we only compare the current day against prices we've already seen, we never buy after we sell.