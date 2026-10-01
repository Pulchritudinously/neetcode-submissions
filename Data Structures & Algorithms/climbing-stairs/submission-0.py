class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)
        
        # return dfs(0) Time: o(2^n) Space: o(n)

        # Bottom Up
        # Idea: To reach step i, you can only come from: step i - 1 (1 step) or i - 2 (2 steps)
        if n <= 2: 
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]