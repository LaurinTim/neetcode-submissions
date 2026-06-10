# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = self.buildSubTree(preorder, inorder)
        return root

    def buildSubTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        val = preorder[0]
        curr_node = TreeNode(val=val)
        inorder_pos = inorder.index(val)
        inorder_left = inorder[:inorder_pos]
        inorder_right = inorder[inorder_pos + 1:]

        curr_node.left = self.buildSubTree(preorder[1:inorder_pos + 1], inorder_left)
        curr_node.right = self.buildSubTree(preorder[inorder_pos + 1:], inorder_right)
        
        return curr_node
