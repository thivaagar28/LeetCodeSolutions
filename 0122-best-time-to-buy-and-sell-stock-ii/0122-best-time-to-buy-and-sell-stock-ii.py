# sum of neighboring peak is always higher than global peak
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
                max_profit += sell-buy #try to make profit from neighbour
            
            buy = sell #whether you make profit or not.. the next neigbour will buy then will be checked with consecutive neighbour

        return max_profit                

        