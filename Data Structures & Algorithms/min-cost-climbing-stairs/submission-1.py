class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def solve(n):

            if n == 0 or n == 1:
                return 0

            if n in memo:
                return memo[n]

            memo[n] = min(
                cost[n-1] + solve(n -1),
                cost[n-2] + solve(n-2)
            )

            return memo[n]

        return solve(len(cost))