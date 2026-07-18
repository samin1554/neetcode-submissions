class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        time = 0

        queue = deque()
        
        while heap or queue:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1 

                if cnt < 0:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap , queue.popleft()[0])

        return time


        