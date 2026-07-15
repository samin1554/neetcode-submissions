class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x , y = point 
            dist = x** 2 + y**2
            heapq.heappush(heap , (-dist , point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [p for d , p in heap]
    