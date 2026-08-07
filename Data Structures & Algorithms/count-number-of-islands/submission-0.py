class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # matrix DFS 
        
        # get grid dimensions so we know our bounds
        rows = len(grid)
        cols = len(grid[0])
        islands = 0 
        
        # visited set -> tracks (row, col) pairs we've already explored,
        # so we don't recount cells or infinite-loop
        visited = set()

        def dfs(row, col):
            # base case / edge cases:
            # - out of bounds (row/col negative or beyond grid dimensions)
            # - already visited this cell
            # - this cell is water ("0")
            # in any of these cases, stop recursing (nothing to explore here)
            if (row < 0 or row >= rows or col < 0 or col >= cols
            or (row, col) in visited
            or grid[row][col] == "0"):
                return

            # mark this land cell as visited so we don't revisit it
            visited.add((row, col))

            # spread to all 4 neighbors (up, left, right, down) to catch
            # every "1" connected to this one, forming the full island
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                dfs(row + dr, col + dc)

        # outer loop -> scan every cell in the grid
        for row in range(rows):
            for col in range(cols):
                # if we find an unvisited land cell, it's the start of a NEW island
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row , col)
        return islands 
        