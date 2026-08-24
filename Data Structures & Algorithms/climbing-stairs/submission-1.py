class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n == 0 or n == 1:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = solve(n-1) + solve(n-2)

            return memo[n]

        return solve(n)