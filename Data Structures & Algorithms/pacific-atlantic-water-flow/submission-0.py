class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # rectangular island with height above sea level at coords [r, c]

        # island borders Pacific Ocean from up and left
        # island borders Atlantic Ocean from down and right

        # water can flow in any direction
        # from a cell to a neighboring cell with lower or equal height

        # find all cells where water can flow to BOTH Atlantic and Pacific

        rows = len(heights)
        cols = len(heights[0])

        track_atlantic, track_pacific = set(), set()

        def dfs(row, col, visited):
            # already visited 
            if (row, col) in visited:
                return

            # mark current cell as visited
            visited.add((row, col))

            # explore all 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + dr
                new_col = col + dc

                # make sure neighbor is inside grid
                # and can be reached in reverse water-flow direction
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and (new_row, new_col) not in visited
                    and heights[new_row][new_col] >= heights[row][col]
                ):
                    dfs(new_row, new_col, visited)

        # Pacific: top
        for col in range(cols):
            dfs(0, col, track_pacific)

        # Pacific: left
        for row in range(rows):
            dfs(row, 0, track_pacific)

        # Atlantic: bottom
        for col in range(cols):
            dfs(rows - 1, col, track_atlantic)

        # Atlantic: right
        for row in range(rows):
            dfs(row, cols - 1, track_atlantic)

        # Find cells reachable from both oceans
        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in track_pacific and (row, col) in track_atlantic:
                    result.append([row, col])

        return result
