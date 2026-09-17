class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # hand has to be sorted
        # then split accordingly to group size 
        if len(hand) % groupSize  != 0:
            return False
        
        hand.sort()

        count = Counter(hand)

        for card in hand:

            if count[card] > 0:
                for i in range(card, card + groupSize):
                    if count[i] == 0:
                        return False
                    
                    count[i] -= 1
        return True


        