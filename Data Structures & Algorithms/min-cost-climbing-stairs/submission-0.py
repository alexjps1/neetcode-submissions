class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # work backwards
        dp = {} # maps index to total cost
        dp[n-1] = cost[n-1]
        dp[n-2] = cost[n-2]
        for i  in range(n - 3, -1, -1):
            # cost of taking current step plus cost of going the rest of the way
            c1 = cost[i] + dp[i+1]
            c2 = cost[i] + dp[i+2]
            dp[i] = min(c1, c2)
        return min(dp[0], dp[1])


