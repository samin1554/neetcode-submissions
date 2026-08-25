class Solution:
    def rob(self, nums: List[int]) -> int:
        # houses are arranged in circle , last and first are adjacent cells
        # so need to find the way to returning [i] which has to be an non adjacent cell 
        # maximum -> prob will have to use max function 

        n = len(nums)

        

        if n == 1:
            return nums[0]



        def solve(start,end):
            length = end - start + 1 # shrinking mechanism for first and last houses

            dp = [0] * length
            dp[0] = nums[start]

            if length > 1:
                dp[1] = max(nums[start],nums[start + 1])
        

            for i in range(2 , length):
                dp[i] = max(dp[i-1],nums[start + i] + dp[i-2])


            return dp[-1]


        case1 = solve(0 , n - 2)
        case2 = solve(1 , n - 1)


        return max(case1 , case2)