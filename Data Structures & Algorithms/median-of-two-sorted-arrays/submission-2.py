class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1 , nums2
        if len(A) > len(B):
            A , B = B , A 

        m = len(A)
        n = len(B)


        half = (m + n + 1) // 2 

        low = 0

        high = m

        while low <= high: 
            i = (low + high) // 2
            j = half - i 


            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                left_max = max(A_left , B_left)
                right_max = min(A_right , B_right)
                if (m + n) % 2 == 1:
                    return float(left_max)
                else:
                    return (left_max + right_max) / 2.0
            
            elif A_left > B_right:
                high = i - 1

            else:
                low = i + 1
