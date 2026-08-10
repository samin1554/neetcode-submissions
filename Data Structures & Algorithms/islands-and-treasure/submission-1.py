from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        INF = 2147483647

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbour_row, neighbour_col = row + dr, col + dc

                if (
                    0 <= neighbour_row < rows
                    and 0 <= neighbour_col < cols
                    and grid[neighbour_row][neighbour_col] == INF
                ):
                    grid[neighbour_row][neighbour_col] = grid[row][col] + 1
                    queue.append((neighbour_row, neighbour_col))
                