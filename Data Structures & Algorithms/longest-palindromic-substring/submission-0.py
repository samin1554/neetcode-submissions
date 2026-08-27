class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        start_index = 0 

        for i in range(len(s)):
            # odd length
            left = i 
            right = i 
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    start_index = left
                    max_len = right - left + 1
                left -= 1
                right += 1



            left = i
            right = i + 1
            while left >=0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    start_index = left
                    max_len = right - left + 1

                left -= 1
                right += 1

        return s[start_index : start_index + max_len]

