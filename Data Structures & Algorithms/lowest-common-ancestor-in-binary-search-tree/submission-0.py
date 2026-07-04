# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def check(p,q, node):
            if root is None:
                return 

            if (p.val > node.val) and (q.val > node.val):
                return self.lowestCommonAncestor(node.right , p , q)

            elif (p.val < node.val ) and (q.val < node.val):
                return self.lowestCommonAncestor(node.left , p , q)

            else:
                return node

            

        return check(p ,q, root)

            

                
        