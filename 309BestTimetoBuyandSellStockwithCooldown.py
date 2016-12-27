class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy[0] = -prices[0]
        ret = 0
        for i in range(1, len(prices)):
            sell[i] = max(buy[i-1] + prices[i], sell[i-1] - prices[i-1] + prices[i])
            if ret < sell[i]:
                ret = sell[i]
            if i == 1:
                buy[i] = buy[0] + prices[0] - prices[i]
            else:
                buy[i] = max(sell[i-2] - prices[i], buy[i-1]+prices[i-1]-prices[i])
        return ret
