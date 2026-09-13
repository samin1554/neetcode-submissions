class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        count = 0 

        current = intervals[0] 

        for i in range(1 , len(intervals)): 
            if current[1] > intervals[i][0]:
                count += 1

                if current[1] > intervals[i][1]:
                    current = intervals[i]
            else:
                current = intervals[i]
                
        return count


        