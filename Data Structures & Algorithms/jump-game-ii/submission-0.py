class Solution:
    def jump(self, nums: List[int]) -> int:
        # nums[i] = max length of a jump towards right from index i 
        # from nums[i] you can jump to any index i + j 
        # j <= nums[i]
        # i + j < nums.lenght

        # initially at nums[0]
        # return minimum number of jumps needed to reach the last index

        target = len(nums) - 1

        jumps = 0 
        scanning_window = 0
        jump_window = 0 

        for i in range(len(nums)):
            if jump_window >= target:
                return jumps

            scanning_window = max(scanning_window, i + nums[i])
            
            if i == jump_window:
                jumps += 1
                jump_window = scanning_window 

        return jumps




