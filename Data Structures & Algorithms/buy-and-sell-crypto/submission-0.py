class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = price
            else:
                diff = price - min_price
                if diff > max_profit:
                    max_profit = diff

        return max_profit
        