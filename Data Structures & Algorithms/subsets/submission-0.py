class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        path = []


        def bt(i):
            
            if i == len(nums): # bottom of tree 

                result.append(path[:])

                return 

            path.append(nums[i])

            bt(i+1)

            path.pop()

            bt(i+1)

        bt(0)

        return result