class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = math.inf
        highestProfit = -math.inf
        for i in prices:
            lowestBuy = min(lowestBuy, i)
            highestProfit = max(i - lowestBuy, highestProfit)
        return highestProfit
