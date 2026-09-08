class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            #base case 
            if i == len(s):
                return True 
            # cache case 
            if i in memo:
                return memo[i]

            # operation
            for word in wordDict:
                if word == s[i:i + len(word)]: # if word matches the first word found 
                    if dfs(i + len(word)): # recursively solve 
                        memo[i] = True 
                        return True 

            memo[i] = False
            return False 

        return dfs(0)
                         
            