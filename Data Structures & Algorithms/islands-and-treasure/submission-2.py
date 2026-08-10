from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        INF = 2147483647

        # traverse through the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:  # find the treasures
                    queue.append((row, col))  # add treasure coordinates to the queue

        while queue:  # while there are cells to process
            row, col = queue.popleft()  # pop the next cell to process

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # check the four neighbors
                neighbour_row, neighbour_col = row + dr, col + dc  # calculate neighbor coordinates

                # make sure the neighbor is inside the grid and is unvisited land
                if (
                    0 <= neighbour_row < rows
                    and 0 <= neighbour_col < cols
                    and grid[neighbour_row][neighbour_col] == INF
                ):  # set neighbor's distance to current cell's distance + 1
                    grid[neighbour_row][neighbour_col] = grid[row][col] + 1
                    # add neighbor to queue so we can process its neighbors later
                    queue.append((neighbour_row, neighbour_col))
                