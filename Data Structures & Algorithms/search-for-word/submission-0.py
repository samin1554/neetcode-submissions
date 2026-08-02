class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_index = 0
        rows = len(board)
        cols = len(board[0])

        used = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, word_index):

            # Base case: we matched the whole word
            if word_index == len(word):
                return True

            # Constraints: outside board
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # Constraints: wrong letter or already used
            if used[row][col] or board[row][col] != word[word_index]:
                return False

            # Choose this cell
            used[row][col] = True

            # Explore neighbours
            found = (
                dfs(row + 1, col, word_index + 1) or  # down
                dfs(row - 1, col, word_index + 1) or  # up
                dfs(row, col + 1, word_index + 1) or  # right
                dfs(row, col - 1, word_index + 1)    # left
            )

            # Undo choice (backtrack)
            used[row][col] = False

            return found

        # Try every possible starting position
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False

        


        