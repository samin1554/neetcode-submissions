"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Create a hashmap 
        hashmap = {}

        #Create a clone function
        def clone(node):
            # clone all nodes of original graph
            if node in hashmap: #if there is a node in the hashmap 
                return hashmap[node] #return that cloned node 

            #make the cloned node 
            copy= Node(node.val) #make initial clone 
            hashmap[node] = copy # add cloned node to hashmap 

            #clone neighbors 
            for neighbor in node.neighbors: # itterate through neighbours of all nodes
                cloned_neighbor = clone(neighbor) #clone the neighbor
                copy.neighbors.append(cloned_neighbor) #add neighbour reference to copy and add to hashmap
            
            return copy
        # edge case 
        if not node:
            return None
        return clone(node)

            
                
        