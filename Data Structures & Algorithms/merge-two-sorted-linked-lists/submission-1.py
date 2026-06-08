# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val: #compare list1 to list 2
                current.next = list1 #Smaller node in list1 attacted to current.next 
                list1 = list1.next # Move list forward 
            else:
                current.next = list2 # smaller node in list2 attacted to current.nexxt
                list2 = list2.next # move list forwards 
            current = current.next  # move current pointer forward 

        if list1:
            current.next = list1 # attach whatever left in list1 
        elif list2:
            current.next = list2 # attach whatever is left in list2
            
        return dummy.next 

