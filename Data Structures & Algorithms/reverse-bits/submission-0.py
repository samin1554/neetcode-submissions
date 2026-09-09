class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 

        for i in range(32):
            bit = (n & 1) #extract right most bit 
            shift_amount = 32 - i - 1 #shifting amount 
            result = result | (bit << shift_amount) # reversed postional shift is added
            n = n >> 1 # move to next bit 

        return result  # return result 

        
        

        