class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n^2) solution
        # return max([max(prices[i:]) - prices[i] for i in range(len(prices))])

        best = 0
        lowest_buy = float('inf')
        for i in range(len(prices)):
            lowest_buy = min(lowest_buy, prices[i])
            best = max(best, prices[i] - lowest_buy)
        return best
