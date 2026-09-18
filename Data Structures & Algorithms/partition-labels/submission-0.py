class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #s = lower case alphabets 

        # split strings into substrings , as many as possible

        # condition , each letter appears at most in 1 sub string 

        # return list of integers representing the size of the substring 

        hashmap = {}
        output = []
        for i in range(len(s)):
            hashmap[s[i]] = i

        start = 0 
        end = 0 


        for i in range(len(s)):
            end = max(end , hashmap[s[i]])


            if i == end:
                size = end - start + 1
                output.append(size)
                start = end + 1
                 

        return output 