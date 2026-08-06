class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        start_index = 0

        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start_index):
            # base case
            if start_index == len(s):
                res.append(path[:])
                return
            # choices
            for end in range(start_index, len(s)):
                substring = s[start_index : end + 1]
        
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res
