class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_fruit = 0 
        minutes = 0 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row , col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1


        while queue and fresh_fruit > 0:

            level_size = len(queue)

            for _ in range(level_size):
                row , col = queue.popleft()
                for dr , dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    fresh_row , fresh_col = row + dr , col + dc
                    if (
                        0 <= fresh_row < rows and 0 <= fresh_col < cols
                        and grid[fresh_row][fresh_col] == 1
                    ):
                        grid[fresh_row][fresh_col] = 2
                        fresh_fruit -= 1
                        queue.append((fresh_row, fresh_col))
            
            minutes += 1

        if fresh_fruit > 0:
            return -1
            
        return minutes 
        
        
                        
