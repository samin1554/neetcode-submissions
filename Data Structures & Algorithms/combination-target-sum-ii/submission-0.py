class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def bt(start, total):
            if total == target:
                result.append(path[:])
                return

            if total > target:
                return
            candidates.sort()
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                bt(i + 1, total + candidates[i])
                path.pop()

        bt(0, 0)
        return result
        