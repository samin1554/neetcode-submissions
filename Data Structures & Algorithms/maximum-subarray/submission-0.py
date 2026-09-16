class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]

        best = nums[0]



        for i in range(1 , len(nums)):
            summation = current + nums[i]
            if summation < nums[i]:
                current = nums[i]
            else:
                current = summation

            if current > best:
                best = current 

        return best 
