class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # from 0 to 4 
        # get the 32 bits of 0 to 4 
        # store the amount of 1s of every number in a list 
        # return list 


        # int -> converted to binary -> do the same where for each number we do an count of how many 1s they have , and we will put that down in a list 
        # the list is as big as 0 to n 

        result = [] 

        for i in range(0 , n + 1):
            count = 0 
            temp = i
            while temp > 0:
                if (temp & 1) == 1:
                    count+= 1
                temp = temp >> 1
            result.append(count)
            

        return result 
