class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # container with the most water = area = index * index 

        # [1,7,2,5,4,7,3,6]
        # output is 36 because , largest water contained is between index 1 and index 7 , which is 
        # output would be 7 * 6 = 42 - (7 - 1) = 36      # this is wrong   
        # area = width x height , 
        # area

        left = 0 
        right = len(heights) - 1 
        max_area = 0

        while left < right:

            max_area = max(max_area , min(heights[left],heights[right]) * (right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return max_area