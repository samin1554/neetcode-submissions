class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # there is a grid , containing Xs and 0s
        # cells are connected to neighbours up down left and right 
        # a region connects every 0 cell 
        # if 0 cell are surrounded up down left and right they turn into Xs 

        # Algo -> 
        # we can maybe operate DFS here instead of BFS, BFS is more targetinng shortest path, but here we care more about traversal and finding 
        # we can alogirthmically find for all 0s and check their neighbour 
        # conditiosn : either be completely surrounded by Xs or Xs and 0s to turn into an X ->
        # if 0s not surounded by up down left and right X or 0 , leave it as it is 

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            if (row, col) in visited:
                return

            if board[row][col] == "X":
                return

            visited.add((row, col))

            for dr, dc in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                dfs(row + dr, col + dc)


        #visit edges 
        for col in range(cols):
            dfs(0 , col)
            dfs(rows - 1, col)

        for row in range(rows):
            dfs(row , 0)
            dfs(row, cols - 1)

        #flip 0s to 1s

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"