class Solution(object):
    def maxProfit(self, prices):
        buy, sell = 0, 1
        maximum_profit = 0

        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maximum_profit = max(maximum_profit, current_profit)
            else:
                buy = sell

            sell += 1

        return maximum_profit
        