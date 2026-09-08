class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}


        def dfs(i , j):

            if i == len(nums):
                return 0 

            if (i , j) in memo:
                return memo[(i , j)]

            skip = dfs(i + 1 , j)

            if j == -1 or nums[i] > nums[j]:
                take = 1 + dfs(i + 1 , i)
            else:
                take = 0 

            result = max(take , skip)
            memo[(i,j)] = result 

            return result 

        return dfs(0 , -1)