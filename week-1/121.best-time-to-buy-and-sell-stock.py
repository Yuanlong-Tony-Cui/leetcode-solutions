class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # NOTE:
        # - The key is to keep track of the min price
        # - Initialize min_price to `float('inf')` so that it then automatically updates to prices[0].

        if len(prices) == 1:
            return 0

        min_price = float('inf')
        max_profit = 0  # no profit by default
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
