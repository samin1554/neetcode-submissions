
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3],[4,6]] old, new = [2,5]

        # 1 --- 3
        #     2 ---- 5
        #          4 --- 6

        intervals.sort()
        output = []

        for interval in intervals:

            # if interval is BEFORE new interval
            if interval[1] < newInterval[0]:
                output.append(interval)

            # if interval is AFTER new interval
            elif interval[0] > newInterval[1]:
                output.append(newInterval)
                newInterval = interval

            # otherwise, they OVERLAP
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        # add the final newInterval
        output.append(newInterval)

        return output


            

        