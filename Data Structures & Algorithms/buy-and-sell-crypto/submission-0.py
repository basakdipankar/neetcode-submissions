class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        max_profit = 0
        buy_price = prices[0]
        for p in prices[1:]:

            if buy_price > p:
                buy_price = p
            else:
                current_profit = p - buy_price
                max_profit = max(current_profit, max_profit)
        return max_profit