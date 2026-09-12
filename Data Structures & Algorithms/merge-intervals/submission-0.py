class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # compare end of first inverval to start of next inverval for each interval 
        

        # sort first 
        intervals.sort()

        # set first inverval as current 

        current = intervals[0] # current interval like [1,3]
        

        output = []

        for i in range(1 , len(intervals)):
            if current[1] >= intervals[i][0]:
                current = [
                    min(current[0], intervals[i][0]),
                    max(current[1], intervals[i][1])
                ]

            else: 
                output.append(current)

                current = intervals[i]

        output.append(current)


        return output 


                
