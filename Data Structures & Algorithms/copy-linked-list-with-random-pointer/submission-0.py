"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head 
        hashmap = {}

        while current:
            new_node = Node(current.val) # Construct a new node 
            hashmap[current] = new_node # maps old nodes to new node 
            current = current.next  # traverse through 

        current = head # back to current head 

        while current: 
            new_node = hashmap[current] # assign node value to current new node 
            new_node.random = hashmap.get(current.random) # assign random node value to current new node 
            new_node.next = hashmap.get(current.next) # assign next node to current new node 
            current = current.next # Traverse 

        return hashmap[head] # return copy 
        