class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        
        def backtrack(open_count , closed_count):

            if len(path) ==  2 * n:
                res.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1 , closed_count)
                path.pop()

            if closed_count < open_count:
                path.append(")")
                backtrack(open_count, closed_count + 1)
                path.pop()

        backtrack(0 , 0)
        return res
            