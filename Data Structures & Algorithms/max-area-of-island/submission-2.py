class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = self.dfs(grid, visited , row , col)
                    if area > max_area:
                        max_area = area
        return max_area

    def dfs(self , grid , visited , row , col):
            rows = len(grid)
            cols = len(grid[0])

            #base case 
            if (
                row < 0 or row >= rows or col < 0 or col >= cols or 
                (row , col) in visited or 
                grid[row][col] == 0
            ):
                return 0 

            visited.add((row, col))
            return 1 + self.dfs(grid , visited , row + 1 , col) \
                     + self.dfs(grid , visited , row - 1 , col) \
                     + self.dfs(grid , visited , row , col + 1) \
                     + self.dfs(grid , visited , row , col - 1)