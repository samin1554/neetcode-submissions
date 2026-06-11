# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def find_mid(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            second_part = slow.next
            slow.next = None
            return head, second_part


        def reverse(head):
            prev = None
            current = head

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev


        first, second = find_mid(head)
        second = reverse(second)

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2




        



            


        