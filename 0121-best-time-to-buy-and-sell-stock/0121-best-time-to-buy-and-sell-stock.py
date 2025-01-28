class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                max_profit = max(max_profit, sell-buy)
            else:
                buy = sell
        
        return max_profit