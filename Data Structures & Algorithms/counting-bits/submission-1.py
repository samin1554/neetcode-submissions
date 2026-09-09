class Solution:
    def countBits(self, n: int) -> List[int]:
        
        

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
