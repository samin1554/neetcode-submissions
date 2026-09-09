class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 # count 

        for i in range(32): # go through all 32 bits 
            if (n & 1) == 1: #if the right most bit is 1 
                count += 1 #increment count 
            n = n >> 1 #shift right to check next number 

        return count  # return total count 

        

    
        # we are given an integer 
        # we have to convert it to 32 bits 
        # get all the 1s from the bits 
