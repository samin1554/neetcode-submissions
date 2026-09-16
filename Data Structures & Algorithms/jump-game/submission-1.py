class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        furthest = 0 

        for i in range(len(nums)):
            #edge case 
            if i > furthest:
                return False 
                
            furthest = max(furthest, i + nums[i])

            if furthest >= target:
                return True
            