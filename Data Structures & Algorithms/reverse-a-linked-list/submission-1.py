# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None 

        # for context : 1 -> 2 -> 3 -> 4 , our head points to 1 so current which is 1 (head)
        # so our previous points to something before our current pointer which is None 

        current = head 

        while current:

            nxt = current.next

            current.next = previous 


            previous = current


            current = nxt 

        return previous






            



            


        