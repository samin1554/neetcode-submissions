class Solution:
    def getSum(self, a: int, b: int) -> int:
        ### XOR -> AND -> left shift 

        ### XOR -> ADDS Without carries

        ### AND -> find carries

        ### left shift --> MOVE CARRIES 
        

        mask =  0xFFFFFFFF # force integers to operate within 32 bit
        max_int = 0x7FFFFFFF 

        while b != 0:
            carry = (a & b) << 1 # AND operation to get carry and shift left operation to carry over the carry 
            a = (a ^ b) & mask # current partial sum 
            b = carry & mask # current carry 

        return a if a <= max_int else ~(a ^ mask)




