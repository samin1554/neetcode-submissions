"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # conflict = end_1 > start_2 
        # no conflict = end_1 =< start_2 
        intervals.sort(key = lambda x: x.start) 

        for i in range(1 , len(intervals)):
            interval_1 = intervals[i-1] # first interval
            interval_2 = intervals[i] # second interval


            if interval_1.end > interval_2.start:
                return False
            
        return True




        

            
