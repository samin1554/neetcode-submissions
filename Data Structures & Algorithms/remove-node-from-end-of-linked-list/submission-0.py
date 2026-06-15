# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        # get length 
        while current:
            count += 1
            current = current.next

        length = count
        index_to_remove = length - n # Node to remove 

        # Edge case , if the target node is the first node remove the node , return the next pointer 
        if index_to_remove == 0:
            return head.next
        
        current = head 
        for _ in range(index_to_remove - 1): #itterate throgh the linked list to find 
            current = current.next # go to node before the target index 

        current.next = current.next.next #skip the target node 

        return head 


        