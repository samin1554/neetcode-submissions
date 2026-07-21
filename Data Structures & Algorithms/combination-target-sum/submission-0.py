class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def bt(start, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i, total + nums[i])
                path.pop()

        bt(0, 0)
        return result





        