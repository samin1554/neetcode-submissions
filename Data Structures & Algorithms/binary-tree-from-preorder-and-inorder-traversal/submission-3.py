# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        left_subtree_inorder = inorder[:mid]
        right_subtree_inorder = inorder[mid + 1:]


        left_subtree_preorder = preorder[1: mid + 1]
        right_subtree_preorder = preorder[mid+1:]

        root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)

        return root
         
        