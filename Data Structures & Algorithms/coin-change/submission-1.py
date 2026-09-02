class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 

        for a_mount in range(1 , amount + 1):
            for c in coins:
                if a_mount - c >= 0:
                    dp[a_mount] = min(dp[a_mount], dp[a_mount - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1
                    


        