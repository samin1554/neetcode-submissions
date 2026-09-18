class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        good_triplets = set()


        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i in range(len(triplet)):
                if triplet[i] == target[i]:
                    good_triplets.add(i)

            if len(good_triplets) == 3:
                 return True

        return False        



        