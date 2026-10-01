class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # array of 10 , 15 , 20 
        # top floor is floor after last so 15 is the cheapest here
        # can't be greedy and always take two steps(not ordered)


        # bottom-up not optimized
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i-1], dp[i - 2] + cost[i - 2])
        
        return dp[n]

        # Time: o(n), Space:o(n)