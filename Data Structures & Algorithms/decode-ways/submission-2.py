class Solution:
    def numDecodings(self, s: str) -> int:
        # uppercase english char which are being encoded by numbers
        # to decode , digits grouped and maped back into letters 
        # input can be 1012 , which can be "10 1 2" which is "JAB" or "10 12" which is JL
        # input cannot be 1 01 2 , which is invalid because contains leading 0 
        # s can only contain digits , return the total number of ways to decode it 


        # dp[i] == max number of ways to get decoded answer 
        #base case 
        # if dp[0] == return -0
        # if dp[i] == return dp[i]

        
        # algorithm 
        # make memory for number 
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0


            result = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                result += dfs(i + 2)

            dp[i] = result
            return result

        return dfs(0)
